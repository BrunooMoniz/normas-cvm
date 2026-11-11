"""Grafo de relações entre normas, tirado só dos cabeçalhos dos .md: sem IA e sem rede.

Grava em grafo/:
  arestas.jsonl         {"de", "para", "relacao", "desde", "fonte"}: a norma `de` age sobre a `para`
  estado.jsonl          {"id", "caminho", "estado", "por"} de cada norma deste acervo
  externos.jsonl        {"id", "url"} das normas citadas que ficam no outro acervo ou no ctresb/leis
  nao_resolvidos.jsonl  ids citados que não têm arquivo em lugar nenhum e trechos sem norma reconhecida

Relações: revoga, revoga_parcial, altera, cita, regulamenta (norma -> lei) e conjunta (a mesma norma no outro acervo).
Uso: python3 scripts/grafo.py (também roda dentro do --relatorio). Arquivo idêntico em normas-bcb e normas-cvm.

Dois índices versionados em scripts/, refeitos à mão quando envelhecem:
  leis_federais.txt.gz    arquivos de federal/ no ctresb/leis (o nome traz a data, que a citação não tem):
    git clone --filter=blob:none --no-checkout --depth 1 https://github.com/ctresb/leis /tmp/leis
    git -C /tmp/leis ls-tree -r --name-only HEAD federal/ \\
      | grep -E '^federal/(leis-ordinarias|leis-complementares|leis-delegadas|decretos-lei|decretos|medidas-provisorias)/.*\\.md$' \\
      | gzip -9n > scripts/leis_federais.txt.gz
  acervo_vizinho.tsv.gz   id e caminho das normas do outro acervo, tirados do grafo/estado.jsonl de lá (no normas-cvm,
                          troque cvm por bcb):
    jq -r '[.id,.caminho]|@tsv' ../normas-cvm/grafo/estado.jsonl | gzip -9n > scripts/acervo_vizinho.tsv.gz
"""
import collections
import datetime as dt
import gzip
import json
import re
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
ACERVO = "cvm" if (AQUI / "cvm.py").exists() else "bcb"
REPOS = {"bcb": "https://github.com/BrunooMoniz/normas-bcb/blob/main/",
         "cvm": "https://github.com/BrunooMoniz/normas-cvm/blob/main/"}
LEIS_URL = "https://github.com/ctresb/leis/blob/main/"
LEIS = {"lei", "lcp", "ldl", "del", "dec", "mpv"}  # os prefixos de arquivo do ctresb/leis
RELACOES = ["revoga", "revoga_parcial", "altera", "cita", "regulamenta", "conjunta"]

# padrão no texto plano -> tipo; o mais específico antes
TIPOS = [
    (r"leis? complementar(?:es)?", "lcp"), (r"leis? delegadas?", "ldl"), (r"decretos? leis?|dl", "del"), (r"medidas? provisorias?|mpv?", "mpv"),
    (r"decretos?|dec", "dec"), (r"leis?", "lei"),
    (r"res[ou]luc(?:ao|oes) conjuntas?", "resolucao-conjunta"), (r"res[ou]luc(?:ao|oes)|res", "resolucao"),
    (r"instruc(?:ao|oes) normativas? conjuntas?", "instrucao-normativa-conjunta"),
    (r"instruc(?:ao|oes) normativas?", "instrucao-normativa"),
    (r"notas? explicativas? a resolucao", "nota-explicativa-resolucao"),
    (r"notas? explicativas?(?: a instrucao)?", "nota-explicativa"), (r"instruc(?:ao|oes)", "instrucao"),
    (r"oficios? circular(?:es)?", "oficio-circular"),
    (r"cartas? circ(?:ular(?:es)?)?", "carta-circular"), (r"circ(?:ular(?:es)?)?", "circular"),
    (r"comunicados? conjuntos?", "comunicado-conjunto"), (r"comunicados?", "comunicado"),
    (r"deliberac(?:ao|oes)", "deliberacao"), (r"parecer(?:es)? de orientacao", "parecer-de-orientacao"),
    (r"portarias? conjuntas?", "portaria-conjunta"), (r"port(?:arias?)?", "portaria"),
    (r"decis(?:ao|oes) conjuntas?", "decisao-conjunta"), (r"atos? normativos? conjuntos?", "ato-normativo-conjunto"),
    (r"atos? do presidente", "ato-do-presidente"), (r"atos? de diretor", "ato-de-diretor"),
]
NUM = r"(\d[\d.]*(?:-\d+)?)"
REF = NUM + r" ?/+ ?(\d{4}|\d{2})(?![\d/])"       # 4.903/2021, 555/14, 1790//98, 2050-11/2000
REF_TITULO = NUM + r"(?: ?/+ ?(\d{4}|\d{2}))?(?![\d/])"  # no título da própria norma o ano pode faltar


def _citacao(ref):
    """tipo + órgão opcional ('BCB', 'BACEN/CVM', 'PTE') + 'nº'/'ns.' opcional + lista de números."""
    ref = re.sub(r"\((?!\?)", "(?:", ref)
    return re.compile(r"\b(?P<tipo>" + "|".join(p for p, _ in TIPOS) + r")\b(?P<orgao>(?: (?:d[aeo] )?[a-z]{2,8}){0,4}?)"
                      r" ?(?:n(?:os?|s)?\b\.? ?)?(?P<refs>" + ref + r"(?:(?:[ ,;]| e )+" + ref + r")*)")


CITA, CITA_TITULO = _citacao(REF), _citacao(REF_TITULO)
DATA = re.compile(r"\b(\d{1,2})o?[/.](\d{1,2})[/.](\d{4}|\d{2})\b")
PARTE = re.compile(r"\b(?:arts?|artigos?|itens|item|incisos?|inc|paragrafos?|parag|alineas?|al|anexos?|capitulos?|"
                   r"cap|secao|secoes|titulos?)\b")
# verbo no começo de uma referência do BCB -> relação da norma do cabeçalho com a citada
VERBOS = [(r'revoga|cancela|torna(?:m)? sem efeito|declara "?em desuso', "revoga"),
          (r"altera|atualiza|prorroga|suspende|revigora|retifica", "altera"),
          (r"regulamenta", "regulamenta"), (r"cita|esclarece|complementa", "cita")]
# palavras que abrem cada trecho das notas da CVM
NOTAS = re.compile(r"\b(ALTERAD[AO]S?|REVOGAD[AO]S?|REVOGA|ALTERA|Altera|Revoga|VIDE|AUDIÊNCIAS? P[ÚU]BLICAS?|"
                   r"CONSULTA PÚBLICA|OBSERVAÇÃO|CANCELAD[AO]S?|DOCUMENTO RELACIONADO|MANIFESTAÇÃO DA SDM)\b")
CONJUNTOS = r"(resolucao-conjunta|decisao-conjunta|comunicado-conjunto)"


def plano(s):
    """Minúsculas sem acento; 'Carta-Circular', 'BCB/CVM' e 'LEI/COMPLEMENTAR' viram palavras soltas."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"(?<=[a-z])[-/]+(?=[a-z])", " ", s)


def ano4(a):
    # shortcut: dois dígitos até 29 são 20xx (as séries daqui começam depois de 1930); rever em 2030
    return a if len(a) == 4 else ("20" if int(a) <= 29 else "19") + a


def sem_datas(t):
    """Tira as datas do texto plano para não virarem número de norma; antes, 'Carta Circular 53 de 6/12/1971' vira '53/1971'."""
    t = re.sub(r"(?<![\d/.])(\d[\d.]*),? de " + DATA.pattern, lambda m: f"{m[1]}/{m[4]}", t)
    return DATA.sub(" ", t)


def desde(t):
    """Data de 'a partir de 1º/5/2021' (texto plano) em AAAA-MM-DD, ou None."""
    m = re.search(r"a partir de (?:de )?" + DATA.pattern, t)
    try:
        return dt.date(int(ano4(m[3])), int(m[2]), int(m[1])).isoformat() if m else None
    except ValueError:
        return None


def ident(tipo, orgao, num, ano, acervo):
    """Id canônico: 'bcb:resolucao-cmn:4903', 'cvm:instrucao:555', 'lei:4595-1964'.
    As séries com numeração própria dispensam o ano; as que recomeçam todo ano (e as leis) levam o ano no id."""
    o = [("bcb" if p in ("bacen", "bc") else p)
         for p in orgao.replace("banco central do brasil", "bcb").split() if p not in ("da", "de", "do")]
    n = "-".join(str(int(p)) for p in num.replace(".", "").split("-"))
    na = f"{n}-{ano4(ano)}"
    cvm = acervo == "cvm"
    if tipo in LEIS:
        return f"{tipo}:{na}"
    if tipo.endswith(("conjunta", "conjunto")):
        if cvm:
            return f"cvm:{'-'.join([tipo] + [p for p in o if p != 'cvm'])}:{na}"
        if not o or {"bcb", "cmn"} & set(o):
            return f"bcb:{tipo}:{n}"
    elif tipo == "resolucao":
        for sigla, serie in (("cvm", "cvm:resolucao"), ("cmn", "bcb:resolucao-cmn"), ("bcb", "bcb:resolucao-bcb"),
                             ("coseg", "bcb:resolucao-coseg"), ("coremec", "bcb:resolucao-coremec")):
            if sigla in o:
                return f"{serie}:{n}"
        if not o:  # sem sigla: no BCB é a série do CMN; na CVM, a Resolução CVM
            return f"cvm:resolucao:{n}" if cvm else f"bcb:resolucao-cmn:{n}"
    elif tipo in ("circular", "carta-circular", "comunicado", "instrucao-normativa", "ato-do-presidente", "ato-de-diretor"):
        if set(o) <= {"bcb"}:
            return f"bcb:{tipo}{'-bcb' if tipo == 'instrucao-normativa' else ''}:{n}"
    elif tipo in ("instrucao", "deliberacao", "parecer-de-orientacao", "nota-explicativa", "nota-explicativa-resolucao"):
        if "cvm" in o or (cvm and not o):
            return f"cvm:{tipo}:{n}"
    elif cvm and tipo == "portaria" and set(o) <= {"cvm", "pte"}:
        return f"cvm:portaria:{na}"
    elif cvm and tipo == "oficio-circular":
        return f"cvm:{'-'.join([tipo] + [p for p in o if p != 'cvm'])}:{na}"
    return f"ext:{'-'.join([tipo] + o)}:{na}"  # norma de outro órgão: não há acervo onde procurar


def citar(t, acervo, ano_padrao=None):
    """Normas citadas num texto plano: [(id, início, fim)]. Com ano_padrao (título da própria norma) o ano é opcional."""
    out = []
    for m in (CITA_TITULO if ano_padrao else CITA).finditer(t):
        tipo = next(nome for p, nome in TIPOS if re.fullmatch(p, m["tipo"]))
        for num, ano in re.findall(REF_TITULO if ano_padrao else REF, m["refs"]):
            out.append((ident(tipo, m["orgao"], num, ano or ano_padrao, acervo), m.start(), m.end()))
    return out


def cabecalho(caminho):
    cab = {}
    with open(caminho, encoding="utf-8") as f:
        if f.readline().rstrip("\n") != "---":
            return cab
        for linha in f:
            linha = linha.rstrip("\n")
            if linha == "---":
                break
            k, _, v = linha.partition(": ")
            try:
                cab[k] = json.loads(v) if v[:1] in '"[' else v
            except ValueError:
                cab[k] = v
    return cab


def id_local(rel, cab, acervo):
    """Id da norma de um arquivo. BCB: o próprio nome ('resolucao-cmn-4839.md'); CVM: tipo e número, ou o título."""
    pasta, _, nome = rel.split("/")
    stem = nome[:-3]
    if acervo == "bcb":
        serie, _, num = stem.rpartition("-")
        return f"bcb:{serie}:{int(num)}"
    tipo = plano(cab.get("tipo", "").removesuffix(" CVM")).replace(" ", "-")
    if tipo in ("instrucao", "resolucao", "deliberacao", "parecer-de-orientacao") and cab.get("numero", "").isdigit():
        return f"cvm:{tipo}:{int(cab['numero'])}"
    achado = citar(plano(cab.get("titulo", "")), "cvm", cab.get("data", "")[:4] or "0000")
    return achado[0][0] if achado else f"cvm:{pasta}:{stem}"


def ler_acervo(raiz, acervo):
    """{id: (caminho relativo, cabeçalho)} das normas (pasta/ano/arquivo.md)."""
    normas = {}
    for md in sorted(raiz.glob("*/*/*.md")):
        rel = md.relative_to(raiz).as_posix()
        if rel[0] in "._" or rel.split("/")[0] in ("scripts", "grafo"):
            continue
        cab = cabecalho(md)
        i = id_local(rel, cab, acervo)
        if i in normas:  # dois arquivos com o mesmo tipo e número: o segundo fica identificado pelo arquivo
            i = f"{acervo}:{rel.split('/')[0]}:{md.stem}"
        normas[i] = (rel, cab)
    return normas


def acoes(t):
    """Relações descritas no texto plano de uma atualização: revogação total, parcial e/ou alteração."""
    if re.search(r"prorrog|revigor|sem efeito a revog", t):  # adia ou desfaz uma revogação: não revoga
        return ["altera"]
    if re.search(r"revogac?ao (?:total|tacita)|revoga est[ae]|sem efeito est[ae]|cancelad|cancelamento dest|em desuso", t):
        return ["revoga"]
    r = ["altera"] if re.search(r"alter|redacao|inclu|acresc|prorrog", t) else []
    if "revog" in t:
        r.append("revoga_parcial")
    return r or ["altera"]


def relacoes_bcb(eu, cab):
    """(de, para, relação, desde, fonte) de um cabeçalho do BCB; ("", campo, texto) para o trecho sem norma."""
    for item in cab.get("atualizacoes") or []:  # quem mexeu nesta norma
        t = plano(item)
        t2 = sem_datas(t)
        # quem atualiza vem no começo; ali o ano pode faltar ('Resolução BCB nº 33 - Revogação total')
        cs = citar(t2, "bcb") or [c for c in citar(t2, "bcb", "0000")[:1] if c[1] == 0 and c[0].startswith("bcb:")]
        if not cs or t.startswith("obs"):  # 'OBS: a Resolução X encontra-se revogada' fala de outra norma
            yield "", "atualizacoes", item
            continue
        for r in acoes(t):
            yield cs[0][0], eu, r, desde(t), "atualizacoes"
    # em que esta norma mexe, o que cita e a base legal; o formato antigo junta frases: 'ALTERA X.   REVOGA Y.'
    for item in (f for bruto in cab.get("referencias") or [] for f in re.split(r"(?<=\.)\s{2,}", bruto)):
        t = plano(item)
        t2 = sem_datas(t)
        cs = citar(t2, "bcb")
        if not cs:
            yield "", "referencias", item
            continue
        verbo = next((r for p, r in VERBOS if re.match(rf"(?:{p})\b", t)), None)
        if re.match(r"atualizad[ao] pel", t):  # raro: a referência conta quem alterou esta norma
            yield cs[0][0], eu, "altera", desde(t), "referencias"
        elif verbo in ("revoga", "altera"):
            ini, fim = cs[0][1], cs[0][2]  # só a lista logo depois do verbo; o resto do texto descreve a mudança
            parcial = verbo == "revoga" and (PARTE.search(t2[:ini]) or PARTE.match(t2[fim:].lstrip(" ,")))
            rels = ["revoga_parcial" if parcial else verbo] + (["revoga_parcial"] if verbo == "altera" and "revog" in t2[fim:] else [])
            for alvo in [c[0] for c in cs if c[1] == ini]:
                for r in rels:
                    yield eu, alvo, r, desde(t), "referencias"
        else:
            for alvo in dict.fromkeys(c[0] for c in cs):
                r = verbo or ("regulamenta" if alvo.split(":")[0] in LEIS else "cita")  # sem verbo: base legal
                yield eu, alvo, r, None, "referencias"


def relacoes_cvm(eu, cab):
    if cab.get("revogada_por"):
        t = plano(cab["revogada_por"])
        cs = citar(sem_datas(t), "cvm")
        if not cs:
            yield "", "revogada_por", cab["revogada_por"]
        for c in cs:
            yield c[0], eu, "revoga", desde(t), "revogada_por"
    partes = NOTAS.split(cab.get("notas") or "")
    for chave, texto in zip(partes[1::2], partes[2::2]):
        k, t = plano(chave), plano(texto)
        t2 = sem_datas(t)
        # 'VIDE Nota Explicativa à Instrução 038' vem sem ano
        cs = citar(t2, "cvm") or [c for c in citar(t2, "cvm", "0000") if c[0].startswith("cvm:nota-explicativa")]
        if k.startswith(("alterad", "revogad")):  # outra norma mexeu nesta
            # 'REVOGADA pela ...' é total; 'REVOGADO o art. 74 pela ...' é parcial
            r = "altera" if k.startswith("alterad") else "revoga" if t2.lstrip().startswith("pel") else "revoga_parcial"
            for c in cs:
                yield c[0], eu, r, desde(t), "notas"
        elif k in ("revoga", "altera", "vide"):  # esta norma mexe em outra, ou só remete a ela
            r = "cita" if k == "vide" else "revoga_parcial" if k == "revoga" and cs and PARTE.search(t2[:cs[0][1]]) else k
            for c in cs:
                yield eu, c[0], r, desde(t) if k != "vide" else None, "notas"
        else:
            continue
        if not cs:
            yield "", "notas", f"{chave}{texto}".strip()


def carregar_indices():
    """(vizinho, leis): {id: caminho no outro acervo} e {id: caminho no ctresb/leis}; vazios se o índice faltar."""
    vizinho, leis = {}, {}
    if (AQUI / "acervo_vizinho.tsv.gz").exists():
        with gzip.open(AQUI / "acervo_vizinho.tsv.gz", "rt", encoding="utf-8") as f:
            vizinho = dict(l.rstrip("\n").split("\t") for l in f if "\t" in l)
    if (AQUI / "leis_federais.txt.gz").exists():
        with gzip.open(AQUI / "leis_federais.txt.gz", "rt", encoding="utf-8") as f:
            for l in f:
                m = re.search(r"/(lei|lcp|ldl|del|dec|mpv)-(\d+(?:-\d+)?)-(\d{4})-\d\d-\d\d\.md$", l)
                if m:
                    leis.setdefault(f"{m[1]}:{m[2]}-{m[3]}", l.strip())
    return vizinho, leis


def montar(raiz=RAIZ, acervo=ACERVO, hoje=None, vizinho=None, leis=None):
    """Lê o acervo e devolve {"arestas", "estado", "externos", "nao_resolvidos", "trechos"} sem gravar nada."""
    hoje = hoje or dt.date.today().isoformat()
    if vizinho is None or leis is None:
        vizinho, leis = carregar_indices()
    normas = ler_acervo(raiz, acervo)
    outro = "cvm" if acervo == "bcb" else "bcb"

    def par_no_bcb(i):
        """'cvm:decisao-conjunta-bcb:13-2003' -> 'bcb:decisao-conjunta:13', se o BCB tem essa norma nesse ano.
        O ano importa: as séries dos dois portais divergem (a Decisão Conjunta 18 do BCB é de 2010; a 18/13 da CVM, outra)."""
        m = re.fullmatch(rf"cvm:{CONJUNTOS}-bcb:(\d+)-(\d{{4}})", i)
        alvo = f"bcb:{m[1]}:{m[2]}" if m else ""
        return alvo if vizinho.get(alvo, "//").split("/")[1] == (m and m[3]) else None

    juntas = {}  # (de, para, relação) -> [datas, fontes]
    exemplo, trechos = {}, collections.Counter()
    exemplo_trecho = {}

    def aresta(de, para, r, d, fonte, texto=""):
        if acervo == "cvm":  # norma conjunta citada que a CVM não publica, mas o BCB sim
            de, para = [i if i in normas else par_no_bcb(i) or i for i in (de, para)]
        if de == para:
            return
        v = juntas.setdefault((de, para, r), [set(), set()])
        v[0].add(d)
        v[1].add(fonte)
        for i in (de, para):
            exemplo.setdefault(i, {"em": de if i == para else para, "campo": fonte})

    extrair = relacoes_cvm if acervo == "cvm" else relacoes_bcb
    for eu, (rel, cab) in normas.items():
        for x in extrair(eu, cab):
            if x[0]:
                aresta(*x)
            else:
                chave = (x[1], re.sub(r"\d[\d./-]*", "N", x[2])[:80])
                trechos[chave] += 1
                exemplo_trecho.setdefault(chave, {"em": eu, "exemplo": x[2][:300]})
        # a mesma norma conjunta no outro acervo
        if acervo == "cvm" and re.fullmatch(rf"cvm:{CONJUNTOS}-bcb:.*", eu):
            if par_no_bcb(eu):
                aresta(eu, par_no_bcb(eu), "conjunta", None, "numero")
            else:
                trechos[("titulo", "conjunta com o BCB sem par no acervo do BCB")] += 1
                exemplo_trecho.setdefault(("titulo", "conjunta com o BCB sem par no acervo do BCB"),
                                          {"em": eu, "exemplo": cab.get("titulo", "")})
        m = acervo == "bcb" and re.fullmatch(rf"bcb:{CONJUNTOS}:(\d+)", eu)
        if m and f"cvm:{m[1]}-bcb:{m[2]}-{rel.split('/')[1]}" in vizinho:
            aresta(eu, f"cvm:{m[1]}-bcb:{m[2]}-{rel.split('/')[1]}", "conjunta", None, "numero")

    # normas_vinculadas (BCB) não diz a relação: vira 'cita', da mais nova para a mais antiga, só onde os campos
    # com verbo não ligaram as duas
    ligadas = {frozenset(k[:2]) for k in juntas}
    for eu, (rel, cab) in normas.items():
        for item in cab.get("normas_vinculadas") or []:
            cs = citar(plano(item), acervo)
            if not cs:
                trechos[("normas_vinculadas", item[:80])] += 1
                exemplo_trecho.setdefault(("normas_vinculadas", item[:80]), {"em": eu, "exemplo": item})
            for c in cs:
                if frozenset((eu, c[0])) not in ligadas:
                    mais_nova = c[0] in normas and str(normas[c[0]][1].get("data", "")) > str(cab.get("data", ""))
                    aresta(*((c[0], eu) if mais_nova else (eu, c[0])), "cita", None, "normas_vinculadas")

    def url(i):
        if i in vizinho:
            return REPOS[outro] + vizinho[i]
        return LEIS_URL + leis[i] if i in leis else None

    arestas = [{"de": de, "para": para, "relacao": r, "desde": min((d for d in v[0] if d), default=None),
                "fonte": "+".join(sorted(v[1]))} for (de, para, r), v in sorted(juntas.items())]
    citados = collections.Counter(i for a in arestas for i in (a["de"], a["para"]) if i not in normas)
    externos = [{"id": i, "url": url(i)} for i in sorted(citados) if url(i)]
    nao = [{"id": i, "arestas": n, **exemplo[i]} for i, n in sorted(citados.items()) if not url(i)]

    # estado: quem tem revogação total em vigor está revogada; quem só foi alterada ou revogada em parte, alterada
    por = collections.defaultdict(lambda: collections.defaultdict(set))
    for a in arestas:
        if a["relacao"] == "revoga" and (a["desde"] or "") <= hoje:
            por[a["para"]]["revogada"].add(a["de"])
        elif a["relacao"] in ("altera", "revoga_parcial") and (a["desde"] or "") <= hoje:
            por[a["para"]]["alterada"].add(a["de"])
    estado = []
    for i, (rel, cab) in sorted(normas.items()):
        # o cabeçalho também vale: o portal marca revogadas (e canceladas) sem dizer por qual norma
        e = "revogada" if por[i]["revogada"] or cab.get("revogada") == "true" or cab.get("cancelada") == "true" \
            else "alterada" if por[i]["alterada"] else "vigente"
        estado.append({"id": i, "caminho": rel, "estado": e, "por": sorted(por[i][e])})
    return {"arestas": arestas, "estado": estado, "externos": externos, "nao_resolvidos": nao,
            "trechos": [{"campo": c, "padrao": p, "trechos": n, **exemplo_trecho[(c, p)]}
                        for (c, p), n in sorted(trechos.items(), key=lambda kv: (-kv[1], kv[0]))]}


def fmt(n):
    return f"{n:,}".replace(",", ".")


def gerar(raiz=RAIZ, acervo=ACERVO):
    """Grava grafo/*.jsonl e devolve as linhas da seção do COBERTURA.md."""
    g = montar(raiz, acervo)
    pasta = raiz / "grafo"
    pasta.mkdir(exist_ok=True)
    for nome, linhas in (("arestas", g["arestas"]), ("estado", g["estado"]), ("externos", g["externos"]),
                         ("nao_resolvidos", g["nao_resolvidos"] + g["trechos"])):
        (pasta / f"{nome}.jsonl").write_text(
            "".join(json.dumps(l, ensure_ascii=False, separators=(",", ":")) + "\n" for l in linhas), encoding="utf-8")
    soltos = {x["id"] for x in g["nao_resolvidos"]}
    por_rel = collections.Counter(a["relacao"] for a in g["arestas"])
    sem = collections.Counter(a["relacao"] for a in g["arestas"] if a["de"] in soltos or a["para"] in soltos)
    total, n_sem = len(g["arestas"]), sum(sem.values())
    situ = collections.Counter(e["estado"] for e in g["estado"])
    pct = (f"{100 * n_sem / total:.1f}".replace(".", ",") + "%") if total else "0%"
    return ["", "## Grafo de relações", "",
            "Gerado por `scripts/grafo.py` a partir dos cabeçalhos, sem IA. Fica em `grafo/`: `arestas.jsonl` (uma relação "
            "por linha), `estado.jsonl` (situação de cada norma), `externos.jsonl` (normas do outro acervo e leis do "
            "ctresb/leis) e `nao_resolvidos.jsonl`.", "",
            "| Relação | Arestas | Não resolvidas |", "| --- | ---: | ---: |",
            *[f"| {r} | {fmt(por_rel[r])} | {fmt(sem[r])} |" for r in RELACOES],
            f"| **Total** | **{fmt(total)}** | **{fmt(n_sem)}** ({pct}) |", "",
            f"Não resolvida = aresta que aponta para uma norma sem arquivo neste acervo, no outro ou no ctresb/leis "
            f"({fmt(len(soltos))} normas distintas). Trechos dos cabeçalhos sem norma reconhecida: "
            f"{fmt(sum(t['trechos'] for t in g['trechos']))}. Situação calculada: {fmt(situ['vigente'])} vigentes, "
            f"{fmt(situ['alterada'])} alteradas e {fmt(situ['revogada'])} revogadas."]


if __name__ == "__main__":
    print("\n".join(gerar()))
