# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13", "mammoth>=1.8"]
# ///
"""Baixa as normas da CVM (conteudo.cvm.gov.br/legislacao) e grava cada uma em Markdown.

Uso:
  uv run scripts/cvm.py                  # índice + normas de todas as categorias
  uv run scripts/cvm.py resolucoes       # só uma categoria
  uv run scripts/cvm.py --limite 20      # amostra (smoke)
  uv run scripts/cvm.py --relatorio      # só regrava COBERTURA.md

Idempotente: o que já está em _fonte/ não é baixado de novo.
"""
import argparse
import datetime as dt
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "_fonte"
INDICE = RAIZ / "_indice"
FALHAS = RAIZ / "_falhas.jsonl"
BASE = "https://conteudo.cvm.gov.br"
UA = "normas-cvm/1.0 (+https://github.com/BrunooMoniz/normas-cvm)"
PAUSA = 0.4  # segundos entre requisições: o portal é público, não precisa de pressa
ORGAO = "Comissão de Valores Mobiliários"

# pasta no portal: (tipo canônico, pasta no repositório)
CATEGORIAS = {
    "resolucoes": ("Resolução CVM", "resolucoes"),
    "instrucoes": ("Instrução CVM", "instrucoes"),
    "deliberacoes": ("Deliberação CVM", "deliberacoes"),
    "pareceres-orientacao": ("Parecer de Orientação CVM", "pareceres-de-orientacao"),
    "oficios-circulares": ("Ofício-Circular CVM", "oficios-circulares"),
    "notas-explicativas": ("Nota Explicativa CVM", "notas-explicativas"),
    "decisoesconjuntas": ("Decisão Conjunta", "decisoes-conjuntas"),
    "portarias": ("Portaria CVM", "portarias"),
    "portaria_conjunta": ("Portaria Conjunta", "portarias-conjuntas"),
}
EXT_TEXTO = {".htm": 0, ".html": 0, ".docx": 1, ".pdf": 2}
MESES = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}


# ---------- rede e cache ----------

def url_abs(href):
    url = urllib.parse.urljoin(BASE + "/", href.strip())
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(p._replace(path=urllib.parse.quote(urllib.parse.unquote(p.path), safe="/")))


def baixar(url, tentativas=4):
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                dados = r.read()
            time.sleep(PAUSA)
            return dados
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 410) or i == tentativas - 1:
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if i == tentativas - 1:
                raise
        time.sleep(5 * (i + 1))


def em_cache(url, forcar=False):
    """Baixa uma vez para _fonte/<caminho do portal>; devolve os bytes."""
    caminho = FONTE / urllib.parse.unquote(urllib.parse.urlsplit(url).path).lstrip("/")
    if caminho.exists() and not forcar:
        return caminho.read_bytes()
    dados = baixar(url)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_bytes(dados)
    return dados


# ---------- índice ----------

def ler_listagem(html):
    """Itens de uma página de resultado da busca de legislação."""
    from bs4 import BeautifulSoup

    sopa = BeautifulSoup(html, "html.parser")
    itens = []
    for art in sopa.select("article"):
        a = art.select_one("h3 a[href]")
        if not a:
            continue
        data = ""
        for p in art.select(".infoItem p"):
            m = re.search(r"Data:\s*(\d{2})/(\d{2})/(\d{4})", p.get_text(" "))
            if m:
                data = f"{m[3]}-{m[2]}-{m[1]}"
        desc = art.select_one(".contentDesc")
        itens.append({
            "href": a["href"].strip(),
            "titulo": " ".join((a.get("title") or a.get_text()).split()),
            "data": data,
            "resumo": " ".join(desc.get_text(" ").split()) if desc else "",
        })
    m = re.search(r"Páginas\s+\d+/(\d+)", html)
    return itens, int(m[1]) if m else 1


def indexar(pasta):
    itens, pagina, total = [], 1, 1
    while pagina <= total:
        q = urllib.parse.urlencode({
            "buscado": "true", "filtro": "todos", "contCategoriasCheck": "1", "itensPagina": "500",
            "pasta": pasta, "vimDaCategoria": f"/legislacao/{pasta}/", "searchPage": str(pagina),
        })
        html = baixar(f"{BASE}/legislacao/index.html?{q}").decode("utf-8", "replace")
        novos, total = ler_listagem(html)
        itens += novos
        pagina += 1
    vistos, unicos = set(), []
    for it in itens:
        if it["href"] not in vistos:
            vistos.add(it["href"])
            unicos.append(it)
    INDICE.mkdir(exist_ok=True)
    (INDICE / f"{pasta}.json").write_text(json.dumps(unicos, ensure_ascii=False, indent=1), encoding="utf-8")
    return unicos


# ---------- página da norma ----------

def data_java(texto):
    """'Fri Dec 23 10:00:00 BRST 2022' -> '2022-12-23'."""
    m = re.search(r"\b([A-Z][a-z]{2}) (\d{1,2}) [\d:]+ \w+ (\d{4})\b", texto or "")
    if not m or m[1] not in MESES:
        return ""
    return f"{m[3]}-{MESES[m[1]]:02d}-{int(m[2]):02d}"


def rank_arquivo(rotulo, href):
    """Menor é melhor: texto consolidado sem marcas > consolidado > original; HTML > DOCX > PDF."""
    r, h = rotulo.lower(), href.lower()
    if "sem marcas" in r:
        versao = 0
    elif "consolid" in r or "consolid" in h:
        versao = 1
    else:
        versao = 2
    return (versao, EXT_TEXTO[Path(urllib.parse.urlsplit(h).path).suffix])


def versao_de(rotulo, href):
    r = rotulo.lower()
    if "sem marcas" in r:
        return "texto consolidado sem marcas"
    if "consolid" in r or "consolid" in href.lower():
        return "texto consolidado"
    if "original" in r:
        return "redação original"
    return "publicação no portal da CVM"


def ler_detalhe(html, url_pagina):
    from bs4 import BeautifulSoup

    sopa = BeautifulSoup(html, "html.parser")
    art = sopa.select_one("article.contentTextoGeral")
    if not art:
        return None
    h2 = art.select_one("h2")
    sec = art.select_one("section.contentArticle") or art
    ps = sec.find_all("p", recursive=False)
    data = data_java(ps[0].get_text(" ")) if ps else ""
    ementa_bruta = ps[1].get_text("\n") if len(ps) > 1 else ""
    pub = re.findall(r"\((?:Publicad[oa]|Republicad[oa]|Retificad[oa])[^)]*\)", sec.get_text(" "))
    ementa = " ".join(re.sub(r"\([^)]*(?:Publicad|Republicad|Retificad)[^)]*\)", " ", ementa_bruta).split())

    # arquivos da própria norma: ficam na tabela de downloads (links do texto apontam para outras normas)
    candidatos = []
    for a in art.select(".boxVejaMais a[href]"):
        href = a["href"].strip()
        ext = Path(urllib.parse.urlsplit(href.lower()).path).suffix
        if ext in EXT_TEXTO and a.get_text(strip=True) and (rank_arquivo(a.get_text(" "), href), a.get_text(" ", strip=True), url_abs(href)) not in candidatos:
            candidatos.append((rank_arquivo(a.get_text(" "), href), a.get_text(" ", strip=True), url_abs(href)))
    if not candidatos:
        # páginas recentes listam "[HTML] / [PDF] / [DOC]" no corpo: aceita só arquivos com o nome da própria norma
        raiz = re.escape(Path(urllib.parse.urlsplit(url_pagina).path).stem.lower())
        for a in sec.select("a[href]"):
            href = a["href"].strip()
            caminho = Path(urllib.parse.unquote(urllib.parse.urlsplit(href.lower()).path))
            if caminho.suffix in EXT_TEXTO and re.match(raiz + r"(?!\d)", caminho.stem):
                candidatos.append((rank_arquivo(a.get_text(" "), href), a.get_text(" ", strip=True) or caminho.name, url_abs(href)))
    candidatos.sort()

    # notas da página (ALTERADA por..., REVOGADA por...): o que vem depois da tabela de downloads
    caixa = art.select_one(".contentVejaMais")
    notas = []
    if caixa:
        for el in caixa.find_next_siblings():
            if el.select_one("#paramForm") or "bottomPrint" in (el.get("class") or []):
                continue  # bloco de temas (gravado à parte) e botão de imprimir
            t = " ".join(el.get_text(" ").split())
            if t:
                notas.append(t)
    texto_notas = " ".join(notas)
    titulo = " ".join(h2.get_text(" ").split()) if h2 else ""
    revogada = "(revogad" in titulo.lower() or bool(re.search(r"\bREVOGAD[AO]\s+(pel|em)", texto_notas))
    # "REVOGADO o art. 74 pela ..." é revogação parcial: só conta "REVOGADA pela <norma>"
    m = re.findall(r"REVOGAD[AO]\s+pel[ao]s?\s+(.+?)(?:\s*\.(?:\s|$)|$)", texto_notas)
    m = [None, m[-1]] if m else None
    return {
        "titulo": titulo,
        "data": data,
        "ementa": ementa,
        "publicacao": "; ".join(p.strip("() ") for p in pub),
        "notas": texto_notas,
        "revogada": revogada,
        "revogada_por": m[1].strip(" .") if (revogada and m) else "",
        "temas": sorted({" ".join(a.get_text(" ").split()) for a in art.select("#paramForm a")} - {""}),
        "arquivos": [{"rotulo": c[1], "url": c[2]} for c in candidatos],
        "fonte": url_pagina,
    }


# ---------- conversão ----------

def limpar_md(md):
    md = md.replace("\xa0", " ").replace("\r", "").replace("\f", "\n")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def html_para_md(html_bytes):
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    if html_bytes[:2] in (b"\xff\xfe", b"\xfe\xff"):  # Word salva "charset=unicode" como UTF-16 com BOM
        html_bytes = html_bytes.decode("utf-16").encode("utf-8")
        html_bytes = re.sub(rb"charset=[\"']?unicode", b"charset=utf-8", html_bytes, flags=re.I)
    cabeca = html_bytes[:4000].decode("ascii", "ignore").lower()
    m = re.search(r"charset=[\"']?([\w-]+)", cabeca)
    try:
        html = html_bytes.decode(m[1] if m else "utf-8")
    except (LookupError, UnicodeDecodeError):
        html = html_bytes.decode("cp1252", "replace")
    sopa = BeautifulSoup(html, "html.parser")
    for t in sopa(["script", "style", "meta", "link", "title", "head"]):
        t.decompose()
    corpo = sopa.body or sopa
    return limpar_md(markdownify(str(corpo), heading_style="ATX", strip=["img", "a"]))


def docx_para_md(dados):
    import mammoth
    from markdownify import markdownify

    html = mammoth.convert_to_html(io.BytesIO(dados)).value
    return limpar_md(markdownify(html, heading_style="ATX", strip=["img", "a"]))


def tessdata():
    """Dados de OCR em português; baixados uma vez para _fonte/tessdata (o sistema só traz inglês)."""
    pasta = FONTE / "tessdata"
    alvo = pasta / "por.traineddata"
    if not alvo.exists():
        pasta.mkdir(parents=True, exist_ok=True)
        alvo.write_bytes(baixar("https://github.com/tesseract-ocr/tessdata_fast/raw/main/por.traineddata"))
    return pasta


def pdf_para_md(dados):
    """Texto do PDF; se vier vazio (escaneado), OCR em português. Devolve (md, ocr?)."""
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "a.pdf"
        pdf.write_bytes(dados)
        texto = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
                               capture_output=True, text=True, timeout=300).stdout
        if len(re.sub(r"\s", "", texto)) >= 200:
            return limpar_md(texto), False
        subprocess.run(["pdftoppm", "-r", "200", "-png", str(pdf), str(Path(tmp) / "p")],
                       check=True, capture_output=True, timeout=900)
        partes = []
        for img in sorted(Path(tmp).glob("p*.png")):
            partes.append(subprocess.run(
                ["tesseract", str(img), "-", "-l", "por", "--tessdata-dir", str(tessdata())],
                capture_output=True, text=True, timeout=300).stdout)
        return limpar_md("\n\n".join(partes)), True


def converter(url, dados):
    ext = Path(urllib.parse.urlsplit(url.lower()).path).suffix
    if ext in (".htm", ".html"):
        return html_para_md(dados), False
    if ext == ".docx":
        return docx_para_md(dados), False
    return pdf_para_md(dados)


# ---------- saída ----------

def slug(href, pasta):
    rel = urllib.parse.unquote(urllib.parse.urlsplit(href).path)
    rel = rel.split(f"/legislacao/{pasta}/", 1)[-1]
    rel = re.sub(r"\.html?$", "", rel)
    partes = rel.split("/")
    # deliberacoes/deli0900/deli908 -> deli908; oficios-circulares/sin/oc-sin-0125 -> oc-sin-0125
    nome = partes[-1] if pasta != "oficios-circulares" or partes[-1].startswith("oc-") else "-".join(partes)
    return re.sub(r"[^\w.-]+", "-", nome).strip("-").lower()


def numero_de(titulo):
    m = re.search(r"\d[\d./-]*", re.sub(r"\(.*?\)", "", titulo))
    return m[0].rstrip("./-") if m else ""


def yaml_str(v):
    return json.dumps(v, ensure_ascii=False)


def montar_md(meta, corpo):
    campos = [
        ("titulo", yaml_str(meta["titulo"])),
        ("orgao", yaml_str(ORGAO)),
        ("tipo", yaml_str(meta["tipo"])),
        ("numero", yaml_str(meta["numero"])),
        ("data", meta["data"]),
        ("ementa", yaml_str(meta["ementa"]) if meta["ementa"] else None),
        ("revogada", "true" if meta["revogada"] else "false"),
        ("revogada_por", yaml_str(meta["revogada_por"]) if meta["revogada_por"] else None),
        ("versao_texto", yaml_str(meta["versao_texto"])),
        ("publicacao", yaml_str(meta["publicacao"]) if meta["publicacao"] else None),
        ("notas", yaml_str(meta["notas"]) if meta["notas"] else None),
        ("temas", yaml_str(meta["temas"]) if meta["temas"] else None),
        ("fonte", yaml_str(meta["fonte"])),
        ("arquivo", yaml_str(meta["arquivo"]) if meta["arquivo"] else None),
        ("sha256_arquivo", meta["sha256_arquivo"] or None),
        ("ocr", "true" if meta["ocr"] else None),
        ("baixado_em", meta["baixado_em"]),
    ]
    cab = "\n".join(f"{k}: {v}" for k, v in campos if v is not None)
    return f"---\n{cab}\n---\n# {meta['titulo']}\n\n{corpo}"


def nomes_unicos(pasta, itens):
    """Slug de cada href; quando dois itens dão o mesmo nome (o portal repete arquivos em subpastas), acrescenta a subpasta."""
    contagem = {}
    for it in itens:
        contagem[slug(it["href"], pasta)] = contagem.get(slug(it["href"], pasta), 0) + 1
    nomes = {}
    for it in itens:
        nome = slug(it["href"], pasta)
        if contagem[nome] > 1:
            sub = urllib.parse.unquote(urllib.parse.urlsplit(it["href"]).path).rstrip("/").split("/")[-2]
            nome = nome + "-" + re.sub(r"[^\w.-]+", "-", sub).lower()
        nomes[it["href"]] = nome
    return nomes


def processar(pasta, item, hoje, forcar=False, nome=None):
    tipo, destino = CATEGORIAS[pasta]
    url = url_abs(item["href"])
    html = em_cache(url, forcar).decode("utf-8", "replace")
    det = ler_detalhe(html, url)
    if det is None:
        raise ValueError("página sem conteúdo (article.contentTextoGeral ausente)")
    titulo = det["titulo"] or item["titulo"]
    data = item["data"] or det["data"]
    corpo, arquivo, sha, ocr, versao = "", "", "", False, "metadados apenas"
    erros = []
    for arq in det["arquivos"]:
        try:
            dados = em_cache(arq["url"], forcar)
            corpo, ocr = converter(arq["url"], dados)
            if len(re.sub(r"\s", "", corpo)) < 40:
                raise ValueError("texto vazio após conversão")
            arquivo, sha, versao = arq["url"], hashlib.sha256(dados).hexdigest(), versao_de(arq["rotulo"], arq["url"])
            break
        except Exception as e:  # tenta o próximo arquivo da lista
            erros.append(f"{arq['url']}: {e}")
            corpo = ""
    if not corpo:
        corpo = "> O portal da CVM não oferece o texto desta norma em HTML, DOCX ou PDF legível; ficaram só os metadados.\n"
    meta = {
        "titulo": titulo, "tipo": tipo, "numero": numero_de(titulo), "data": data,
        "ementa": det["ementa"] or item["resumo"], "revogada": det["revogada"],
        "revogada_por": det["revogada_por"], "versao_texto": versao, "publicacao": det["publicacao"],
        "notas": det["notas"], "temas": det["temas"], "fonte": url, "arquivo": arquivo, "sha256_arquivo": sha, "ocr": ocr,
        "baixado_em": hoje,
    }
    ano = data[:4] if data else "sem-data"
    saida = RAIZ / destino / ano / f"{nome or slug(item['href'], pasta)}.md"
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(montar_md(meta, corpo), encoding="utf-8")
    return saida, (erros if not arquivo else [])


# ---------- relatório ----------

def relatorio():
    falhas = [json.loads(l) for l in FALHAS.read_text(encoding="utf-8").splitlines()] if FALHAS.exists() else []
    linhas = ["# Cobertura", "", "Gerado por `scripts/cvm.py --relatorio`. Índice = itens na busca oficial do portal da CVM.", "",
              "| Categoria | Índice | Arquivos .md | Com texto | Só metadados | Falhas |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    tot = [0] * 5
    for pasta, (tipo, destino) in CATEGORIAS.items():
        idx = len(json.loads((INDICE / f"{pasta}.json").read_text(encoding="utf-8"))) if (INDICE / f"{pasta}.json").exists() else 0
        mds = list((RAIZ / destino).rglob("*.md"))
        sem = sum(1 for p in mds if 'versao_texto: "metadados apenas"' in p.read_text(encoding="utf-8")[:6000])
        nf = sum(1 for f in falhas if f["pasta"] == pasta)
        vals = [idx, len(mds), len(mds) - sem, sem, nf]
        tot = [a + b for a, b in zip(tot, vals)]
        linhas.append(f"| {tipo} (`{destino}/`) | " + " | ".join(f"{v:,}".replace(",", ".") for v in vals) + " |")
    linhas.append("| **Total** | " + " | ".join(f"**{v:,}**".replace(",", ".") for v in tot) + " |")
    (RAIZ / "COBERTURA.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    import readme  # números do README e progresso.svg saem da mesma medição
    readme.main(readme.CONFIG)
    return tot


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pastas", nargs="*", help=f"categorias (padrão: todas): {', '.join(CATEGORIAS)}")
    ap.add_argument("--limite", type=int, help="processa só as N primeiras de cada categoria")
    ap.add_argument("--forcar", action="store_true", help="baixa de novo mesmo o que está em cache")
    ap.add_argument("--relatorio", action="store_true", help="só regrava COBERTURA.md")
    a = ap.parse_args()
    if a.relatorio:
        print(relatorio())
        return
    hoje = dt.date.today().isoformat()
    pastas = a.pastas or list(CATEGORIAS)
    anteriores = [json.loads(l) for l in FALHAS.read_text(encoding="utf-8").splitlines()] if FALHAS.exists() else []
    falhas = [f for f in anteriores if f["pasta"] not in pastas]
    for pasta in pastas:
        itens = indexar(pasta)
        nomes = nomes_unicos(pasta, itens)
        if a.limite:
            itens = itens[: a.limite]
        print(f"{pasta}: {len(itens)} itens", flush=True)
        for n, item in enumerate(itens, 1):
            try:
                _, avisos = processar(pasta, item, hoje, a.forcar, nomes[item["href"]])
                if avisos:
                    falhas.append({"pasta": pasta, "href": item["href"], "erro": "sem texto: " + " | ".join(avisos)})
            except Exception as e:
                falhas.append({"pasta": pasta, "href": item["href"], "erro": f"{type(e).__name__}: {e}"})
            if n % 50 == 0:
                print(f"  {pasta}: {n}/{len(itens)}", flush=True)
    falhas.sort(key=lambda f: (f["pasta"], f["href"]))
    FALHAS.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in falhas), encoding="utf-8")
    print("total [índice, md, com texto, só metadados, falhas]:", relatorio())


if __name__ == "__main__":
    sys.exit(main())
