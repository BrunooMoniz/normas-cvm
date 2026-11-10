"""Regrava os números do acervo no README.md (entre <!-- acervo:inicio --> e <!-- acervo:fim -->) e o progresso.svg.

Só biblioteca padrão: lê o cabeçalho YAML de cada .md e os totais do índice em COBERTURA.md.
Uso: python3 scripts/readme.py
"""
import collections
import datetime as dt
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INICIO, FIM = "<!-- acervo:inicio -->", "<!-- acervo:fim -->"
IGNORAR = {"scripts", "_fonte", "_indice", ".git", ".venv"}


def fmt(n):
    return f"{n:,}".replace(",", ".")


def pct(a, b):
    return f"{100 * a / b:.1f}".replace(".", ",") + "%" if b else "0%"


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
    cab = texto[4:texto.find("\n---\n", 4)]
    campos = {}
    for linha in cab.splitlines():
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


def lista_yaml(v):
    return re.findall(r'"([^"]+)"', v or "")


def tabela(cab, linhas, alinhar=None):
    """alinhar: 'e' (esquerda) ou 'd' (direita) por coluna; padrão: primeira à esquerda, resto à direita."""
    alinhar = alinhar or "e" + "d" * (len(cab) - 1)
    out = ["| " + " | ".join(cab) + " |", "| " + " | ".join("---:" if a == "d" else "---" for a in alinhar) + " |"]
    out += ["| " + " | ".join(str(c) for c in l) + " |" for l in linhas]
    return "\n".join(out)


def svg(feitas, total):
    p = feitas / total if total else 0
    rotulo = f"{pct(feitas, total)} · {fmt(feitas)} de {fmt(total)} normas"
    largura = 420
    barra = max(0, round((largura - 4) * p))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="28" role="img" aria-label="Progresso do acervo: {rotulo}">
  <title>Progresso do acervo: {rotulo}</title>
  <rect width="{largura}" height="28" rx="6" fill="#e5e7eb"/>
  <rect x="2" y="2" width="{barra}" height="24" rx="5" fill="#2563eb"/>
  <text x="{largura / 2}" y="18.5" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="12" fill="#111827" stroke="#ffffff" stroke-width="3" paint-order="stroke">{rotulo}</text>
</svg>
"""


def bloco(normas, indice, rotulo_extra, campo_extra):
    hoje = dt.date.today().strftime("%d/%m/%Y")
    total_idx = sum(indice.values()) or len(normas)
    por_pasta = collections.defaultdict(list)
    for n in normas:
        por_pasta[n["_pasta"]].append(n)
    pastas = sorted(set(por_pasta) | set(indice), key=lambda p: -indice.get(p, len(por_pasta[p])))

    linhas, tot = [], [0, 0, 0, 0]
    for p in pastas:
        ns = por_pasta.get(p, [])
        tipos = sorted({n.get("tipo", "") for n in ns}) or ["(ainda não coletado)"]
        rev = sum(1 for n in ns if n.get("revogada") == "true" or n.get("cancelada") == "true")
        datas = sorted(n["data"] for n in ns if n.get("data"))
        idx = indice.get(p, len(ns))
        tot = [tot[0] + idx, tot[1] + len(ns), tot[2] + len(ns) - rev, tot[3] + rev]
        linhas.append([f"[`{p}/`]({p}/)", ", ".join(tipos), fmt(idx), fmt(len(ns)), fmt(len(ns) - rev), fmt(rev),
                       datas[0][:4] if datas else "", datas[-1][:4] if datas else ""])
    linhas.append(["**Total**", "", f"**{fmt(tot[0])}**", f"**{fmt(tot[1])}**", f"**{fmt(tot[2])}**", f"**{fmt(tot[3])}**", "", ""])

    decadas = collections.Counter()
    rev_dec = collections.Counter()
    for n in normas:
        if n.get("data"):
            d = n["data"][:3] + "0"
            decadas[d] += 1
            rev_dec[d] += n.get("revogada") == "true"
    maior = max(decadas.values(), default=1)
    lin_dec = [[f"{d}s", fmt(c), fmt(c - rev_dec[d]), "█" * max(1, round(20 * c / maior))] for d, c in sorted(decadas.items())]

    extra = collections.Counter()
    for n in normas:
        valor = n.get(campo_extra, "")
        for v in (lista_yaml(valor) if valor.startswith("[") else [valor] if valor else []):
            extra[v] += 1
    lin_extra = [[v, fmt(c)] for v, c in extra.most_common(15)]

    feitas = len(normas)
    partes = [
        INICIO,
        f"[![progresso](progresso.svg)](COBERTURA.md)",
        "",
        f"**{fmt(feitas)} de {fmt(total_idx)} normas do índice oficial ({pct(feitas, total_idx)})**, "
        f"números de {hoje}. Vigentes são as que o portal não marca como revogadas nem canceladas.",
        "",
        "### Por pasta",
        "",
        tabela(["Pasta", "Tipo", "No índice oficial", "Publicadas", "Vigentes", "Revogadas", "De", "Até"], linhas, "eedddddd"),
        "",
        "### Por década",
        "",
        tabela(["Década", "Normas", "Vigentes", "Distribuição"], lin_dec, "edde"),
    ]
    if lin_extra:
        partes += ["", f"### {rotulo_extra}", "", tabela([rotulo_extra.split(' ')[0], "Normas"], lin_extra)]
    partes += ["", FIM]
    return "\n".join(partes), feitas, total_idx


def main(rotulo_extra, campo_extra):
    normas = ler_acervo()
    texto, feitas, total = bloco(normas, indice_por_pasta(), rotulo_extra, campo_extra)
    readme = RAIZ / "README.md"
    atual = readme.read_text(encoding="utf-8") if readme.exists() else ""
    i, j = atual.find(INICIO), atual.find(FIM)
    if i < 0 or j < 0:  # cópia de coleta (ex.: VM) sem README: não é erro
        print("README.md sem os marcadores <!-- acervo:inicio --> e <!-- acervo:fim -->; nada a regravar")
        return
    readme.write_text(atual[:i] + texto + atual[j + len(FIM):], encoding="utf-8")
    (RAIZ / "progresso.svg").write_text(svg(feitas, total), encoding="utf-8")
    print(f"README e progresso.svg: {feitas} de {total}")


if __name__ == "__main__":
    main("Temas mais frequentes", "temas")
