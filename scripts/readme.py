"""Regrava os números do acervo no README.md (entre <!-- acervo:inicio --> e <!-- acervo:fim -->),
o painel progresso.svg e o gráfico decadas.svg.

Só biblioteca padrão: lê o cabeçalho YAML de cada .md e os totais do índice em COBERTURA.md.
Uso: python3 scripts/readme.py
"""
import collections
import datetime as dt
import re
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent
INICIO, FIM = "<!-- acervo:inicio -->", "<!-- acervo:fim -->"
IGNORAR = {"scripts", "_fonte", "_indice", ".git", ".venv"}

# paleta do GitHub escuro, a mesma do painel do ctresb/leis
FUNDO, TRILHO, LINHA = "#0d1117", "#21262d", "#30363d"
TEXTO, APAGADO, AZUL, VERDE = "#e6edf3", "#8b949e", "#58a6ff", "#3fb950"
FONTE = "-apple-system,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"


def fmt(n):
    return f"{n:,}".replace(",", ".")


def pct(a, b):
    return (f"{100 * a / b:.1f}".replace(".", ",") + "%") if b else "0%"


def indice_por_pasta():
    """Coluna 'Índice' de COBERTURA.md, por pasta (a pasta vem entre crases)."""
    out = {}
    cob = RAIZ / "COBERTURA.md"
    for linha in cob.read_text(encoding="utf-8").splitlines() if cob.exists() else []:
        m = re.search(r"`([\w-]+)/`", linha)
        nums = [c.strip() for c in linha.split("|") if re.fullmatch(r"\s*[\d.]+\s*", c)]
        if m and nums:
            out[m[1]] = int(nums[0].replace(".", ""))
    return out


def cabecalho(texto):
    if not texto.startswith("---\n"):
        return {}
    campos = {}
    for linha in texto[4:texto.find("\n---\n", 4)].splitlines():
        k, _, v = linha.partition(": ")
        campos[k] = v.strip().strip('"')
    return campos


def ler_acervo():
    normas = []
    for pasta in sorted(p for p in RAIZ.iterdir() if p.is_dir() and p.name not in IGNORAR and not p.name.startswith(".")):
        for md in pasta.rglob("*.md"):
            with md.open(encoding="utf-8") as f:
                c = cabecalho(f.read(6000))
            if c:
                c["_pasta"] = pasta.name
                normas.append(c)
    return normas


def revogada(n):
    return n.get("revogada") == "true" or n.get("cancelada") == "true"


def tabela(cab, linhas, alinhar=None):
    """alinhar: 'e' (esquerda) ou 'd' (direita) por coluna; padrão: primeira à esquerda, resto à direita."""
    alinhar = alinhar or "e" + "d" * (len(cab) - 1)
    out = ["| " + " | ".join(cab) + " |", "| " + " | ".join("---:" if a == "d" else "---" for a in alinhar) + " |"]
    out += ["| " + " | ".join(str(c) for c in l) + " |" for l in linhas]
    return "\n".join(out)


# ---------- painel de progresso (progresso.svg) ----------

def t(x, y, s, tam=13, cor=TEXTO, peso=None, ancora=None, fonte=None):
    attrs = f'x="{x}" y="{y}" font-size="{tam}" fill="{cor}"'
    if peso:
        attrs += f' font-weight="{peso}"'
    if ancora:
        attrs += f' text-anchor="{ancora}"'
    if fonte:
        attrs += f' font-family="{fonte}"'
    return f"<text {attrs}>{escape(s)}</text>"


def barra(x, y, larg, alt, frac, cor):
    cheio = 0 if frac <= 0 else max(alt, round(larg * min(frac, 1)))
    out = f'<rect x="{x}" y="{y}" width="{larg}" height="{alt}" rx="{alt / 2}" fill="{TRILHO}"/>'
    if cheio:
        out += f'<rect x="{x}" y="{y}" width="{cheio}" height="{alt}" rx="{alt / 2}" fill="{cor}"/>'
    return out


def painel(titulo, grupos, nomes, feitos, indice, revog, hoje):
    W, ESQ, DIR, BX, BW = 1180, 24, 1156, 430, 470
    total, pronto = sum(indice.values()), sum(feitos.values())
    vig = pronto - sum(revog.values())
    els = [f'<rect width="{W}" height="__H__" fill="{FUNDO}"/>',
           t(ESQ, 40, titulo, 21, peso="700"),
           t(ESQ, 62, f"{fmt(pronto)} normas em Markdown · {fmt(vig)} vigentes · {fmt(pronto - vig)} revogadas", 12.5),
           t(ESQ, 82, f"Percentual sobre o índice oficial · {fmt(pronto)} / {fmt(total)}", 12, APAGADO),
           t(DIR, 82, pct(pronto, total), 13, VERDE if pronto >= total else AZUL, ancora="end"),
           barra(ESQ, 98, DIR - ESQ, 16, pronto / total if total else 0, VERDE if pronto >= total else AZUL)]
    y = 152
    for nome_grupo, sub, pastas in grupos:
        pastas = [p for p in pastas if p in indice]
        if not pastas:
            continue
        gi, gf = sum(indice[p] for p in pastas), sum(feitos.get(p, 0) for p in pastas)
        els += [f'<rect x="0" y="{y}" width="{W}" height="1" fill="{LINHA}"/>',
                t(ESQ, y + 22, nome_grupo.upper(), 12.5, peso="700"),
                t(BX, y + 22, sub, 11, APAGADO),
                t(DIR, y + 22, pct(gf, gi), 12.5, VERDE if gf >= gi else AZUL, ancora="end")]
        y += 51
        for p in pastas:
            f, i = feitos.get(p, 0), indice[p]
            cor = VERDE if f >= i else AZUL
            els += [t(ESQ, y, nomes.get(p, p), 13, peso="600"),
                    barra(BX, y - 9, BW, 9, f / i if i else 0, cor),
                    t(916, y, f"{fmt(f)} / {fmt(i)}", 11, APAGADO, fonte=MONO),
                    t(DIR, y, pct(f, i), 11.5, cor, "600", "end", MONO)]
            y += 22
        y += 8
    els += [f'<rect x="0" y="{y}" width="{W}" height="1" fill="{LINHA}"/>',
            t(ESQ, y + 30, f"Atualizado em {hoje} · índice contado na busca oficial do portal", 11, APAGADO)]
    h = y + 52
    corpo = "".join(els).replace("__H__", str(h))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
            f'font-family="{FONTE}" role="img" aria-label="{escape(titulo)}: {pct(pronto, total)}">'
            f"<title>{escape(titulo)}: {fmt(pronto)} de {fmt(total)}</title>{corpo}</svg>\n")


# ---------- gráfico por década (decadas.svg) ----------

def grafico_decadas(titulo, normas, hoje):
    vig, rev = collections.Counter(), collections.Counter()
    for n in normas:
        if n.get("data"):
            d = int(n["data"][:3] + "0")
            (rev if revogada(n) else vig)[d] += 1
    decadas = sorted(set(vig) | set(rev))
    W, H, ESQ, DIR, TOPO, BASE = 1180, 360, 24, 1156, 96, 300
    maior = max((vig[d] + rev[d] for d in decadas), default=1)
    passo = (DIR - ESQ) / max(len(decadas), 1)
    col = min(70, passo * 0.62)
    els = [f'<rect width="{W}" height="{H}" fill="{FUNDO}"/>',
           t(ESQ, 40, titulo, 21, peso="700"),
           t(ESQ, 62, "Normas por década da edição", 12.5),
           f'<rect x="{DIR - 200}" y="52" width="10" height="10" rx="2" fill="{AZUL}"/>',
           t(DIR - 184, 61, "vigentes", 11.5, APAGADO),
           f'<rect x="{DIR - 110}" y="52" width="10" height="10" rx="2" fill="{LINHA}"/>',
           t(DIR - 94, 61, "revogadas", 11.5, APAGADO),
           f'<rect x="{ESQ}" y="{BASE}" width="{DIR - ESQ}" height="1" fill="{LINHA}"/>']
    for k, d in enumerate(decadas):
        cx = ESQ + passo * k + passo / 2
        x = round(cx - col / 2, 1)
        hv = (BASE - TOPO) * vig[d] / maior
        hr = (BASE - TOPO) * rev[d] / maior
        if hr:
            els.append(f'<rect x="{x}" y="{BASE - hv - hr:.1f}" width="{col:.1f}" height="{hr:.1f}" fill="{LINHA}"/>')
        if hv:
            els.append(f'<rect x="{x}" y="{BASE - hv:.1f}" width="{col:.1f}" height="{hv:.1f}" fill="{AZUL}"/>')
        els += [t(round(cx), round(BASE - hv - hr - 8), fmt(vig[d] + rev[d]), 11.5, TEXTO, "600", "middle", MONO),
                t(round(cx), BASE + 20, f"{d}s", 12, APAGADO, ancora="middle")]
    els.append(t(ESQ, H - 14, f"Atualizado em {hoje}", 11, APAGADO))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'font-family="{FONTE}" role="img" aria-label="{escape(titulo)}"><title>{escape(titulo)}</title>'
            + "".join(els) + "</svg>\n")


# ---------- README ----------

def bloco(normas, indice, nomes, rotulo_extra, campo_extra, hoje):
    por_pasta = collections.defaultdict(list)
    for n in normas:
        por_pasta[n["_pasta"]].append(n)
    pastas = sorted(set(por_pasta) | set(indice), key=lambda p: -indice.get(p, len(por_pasta[p])))
    linhas, tot = [], [0, 0, 0, 0]
    for p in pastas:
        ns = por_pasta.get(p, [])
        rev = sum(1 for n in ns if revogada(n))
        datas = sorted(n["data"] for n in ns if n.get("data"))
        idx = indice.get(p, len(ns))
        tot = [tot[0] + idx, tot[1] + len(ns), tot[2] + len(ns) - rev, tot[3] + rev]
        linhas.append([f"[{nomes.get(p, p)}]({p}/)", fmt(idx), fmt(len(ns)), fmt(len(ns) - rev), fmt(rev),
                       f"{datas[0][:4]} a {datas[-1][:4]}" if datas else ""])
    linhas.append(["**Total**", f"**{fmt(tot[0])}**", f"**{fmt(tot[1])}**", f"**{fmt(tot[2])}**", f"**{fmt(tot[3])}**", ""])

    extra = collections.Counter()
    for n in normas:
        v = n.get(campo_extra, "")
        for item in (re.findall(r'"([^"]+)"', v) if v.startswith("[") else [v] if v else []):
            extra[item] += 1
    partes = [INICIO,
              "[![Progresso do acervo](progresso.svg)](COBERTURA.md)", "",
              "### Por série", "",
              tabela(["Série", "No índice oficial", "Publicadas", "Vigentes", "Revogadas", "Período"], linhas, "eddddd"), "",
              "Vigentes são as que o portal não marca como revogadas nem canceladas.", "",
              "### Por década", "",
              "![Normas por década](decadas.svg)"]
    if extra:
        cab = rotulo_extra.split(" ")[0]
        partes += ["", f"### {rotulo_extra}", "", tabela([cab, "Normas"], [[k, fmt(c)] for k, c in extra.most_common(15)])]
    partes += ["", f"_Números de {hoje}, gerados por `scripts/readme.py`._", FIM]
    return "\n".join(partes)


def main(cfg):
    hoje = dt.date.today().strftime("%d/%m/%Y")
    normas, indice = ler_acervo(), indice_por_pasta()
    if not indice:
        indice = dict(collections.Counter(n["_pasta"] for n in normas))
    feitos = collections.Counter(n["_pasta"] for n in normas)
    revog = collections.Counter(n["_pasta"] for n in normas if revogada(n))
    listadas = {p for _, _, ps in cfg["grupos"] for p in ps}
    grupos = cfg["grupos"] + [("Outras séries", "", sorted(set(indice) - listadas))]
    (RAIZ / "progresso.svg").write_text(painel(cfg["titulo"], grupos, cfg["nomes"], feitos, indice, revog, hoje), encoding="utf-8")
    (RAIZ / "decadas.svg").write_text(grafico_decadas(cfg["titulo_decadas"], normas, hoje), encoding="utf-8")
    readme = RAIZ / "README.md"
    atual = readme.read_text(encoding="utf-8") if readme.exists() else ""
    i, j = atual.find(INICIO), atual.find(FIM)
    if i < 0 or j < 0:  # cópia de coleta (ex.: VM) sem README: não é erro
        print("README.md sem os marcadores <!-- acervo:inicio --> e <!-- acervo:fim -->; só os SVGs foram regravados")
        return
    texto = bloco(normas, indice, cfg["nomes"], cfg["rotulo_extra"], cfg["campo_extra"], hoje)
    readme.write_text(atual[:i] + texto + atual[j + len(FIM):], encoding="utf-8")
    print(f"README, progresso.svg e decadas.svg: {len(normas)} de {sum(indice.values())}")


CONFIG = {
    "titulo": "Acervo das normas da CVM",
    "titulo_decadas": "Normas da CVM por década",
    "rotulo_extra": "Temas mais frequentes",
    "campo_extra": "temas",
    "grupos": [
        ("Atos normativos", "Colegiado da CVM", ["resolucoes", "instrucoes", "deliberacoes", "pareceres-de-orientacao"]),
        ("Orientação das áreas técnicas", "superintendências e notas explicativas", ["oficios-circulares", "notas-explicativas"]),
        ("Atos conjuntos e administrativos", "BCB, CADE, Ministério da Fazenda e Presidência da CVM",
         ["decisoes-conjuntas", "portarias", "portarias-conjuntas"]),
    ],
    "nomes": {
        "resolucoes": "Resoluções CVM", "instrucoes": "Instruções CVM", "deliberacoes": "Deliberações CVM",
        "pareceres-de-orientacao": "Pareceres de Orientação", "oficios-circulares": "Ofícios-Circulares",
        "notas-explicativas": "Notas Explicativas", "decisoes-conjuntas": "Decisões Conjuntas",
        "portarias": "Portarias CVM", "portarias-conjuntas": "Portarias Conjuntas",
    },
}

if __name__ == "__main__":
    main(CONFIG)
