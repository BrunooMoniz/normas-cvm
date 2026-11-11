# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13", "mammoth>=1.8"]
# ///
"""Testes do conversor da CVM. Rodar: uv run scripts/test_cvm.py"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cvm  # noqa: E402
import grafo  # noqa: E402

FIX = Path(__file__).parent / "fixtures"


class Basicos(unittest.TestCase):
    def test_data_java(self):
        self.assertEqual(cvm.data_java("Fri Dec 23 10:00:00 BRST 2022"), "2022-12-23")
        self.assertEqual(cvm.data_java("sem data"), "")

    def test_numero(self):
        self.assertEqual(cvm.numero_de("Instrução CVM 409 (Revogada)"), "409")
        self.assertEqual(cvm.numero_de("Ofício Circular CVM/SIN 01/25"), "01/25")

    def test_slug(self):
        self.assertEqual(cvm.slug("/legislacao/deliberacoes/deli0900/deli908.html", "deliberacoes"), "deli908")
        self.assertEqual(cvm.slug("/legislacao/oficios-circulares/sin/oc-sin-0125.html", "oficios-circulares"), "oc-sin-0125")

    def test_nomes_unicos_em_colisao(self):
        itens = [{"href": "/legislacao/oficios-circulares/sin/oc-sin-0623.html"},
                 {"href": "/legislacao/oficios-circulares/sse1/oc-sin-0623.html"},
                 {"href": "/legislacao/oficios-circulares/sin/oc-sin-0125.html"}]
        nomes = cvm.nomes_unicos("oficios-circulares", itens)
        self.assertEqual(len(set(nomes.values())), 3)
        self.assertEqual(nomes[itens[1]["href"]], "oc-sin-0623-sse1")
        self.assertEqual(nomes[itens[2]["href"]], "oc-sin-0125")

    def test_html_utf16_do_word(self):
        html = '<html><head><meta http-equiv=Content-Type content="text/html; charset=unicode"></head><body><p>Resolução CVM nº 218</p></body></html>'
        md = cvm.html_para_md(html.encode("utf-16"))
        self.assertIn("Resolução CVM nº 218", md)

    def test_citacao_na_ementa(self):
        achados = cvm.CITACAO.findall("Altera a Resolução CVM nº 60, de 23 de dezembro de 2021 e a Instrução CVM n° 555.")
        self.assertEqual(achados, [("Resolução", "60"), ("Instrução", "555")])

    def test_rank_prefere_consolidado_sem_marcas_e_html(self):
        arqs = [("Instrução (redação original)", "a/inst1.pdf"), ("Instrução (texto consolidado)", "a/inst1consolid.pdf"),
                ("Instrução (texto consolidado) [DOC]", "a/inst1consolid.docx"),
                ("Instrução (texto consolidado sem marcas)", "a/inst1consolid_sm.pdf")]
        melhor = min(arqs, key=lambda a: cvm.rank_arquivo(*a))
        self.assertIn("sem marcas", melhor[0])
        self.assertLess(cvm.rank_arquivo("[HTML]", "x.htm"), cvm.rank_arquivo("[PDF]", "x.pdf"))

    def test_listagem(self):
        html = """<article><h3><a href="/legislacao/resolucoes/resol247.html" title="Resolução CVM 247"> Resolução CVM 247</a></h3>
        <div class="contentDesc">Altera a Resolução CVM nº 60.</div><div class="infoItem"><p><b>Data:</b> 02/10/2026</p></div></article>
        <span>Páginas 1/3</span>"""
        itens, paginas = cvm.ler_listagem(html)
        self.assertEqual(paginas, 3)
        self.assertEqual(itens[0]["data"], "2026-10-02")
        self.assertEqual(itens[0]["href"], "/legislacao/resolucoes/resol247.html")


class PaginasReais(unittest.TestCase):
    def test_layout_com_tabela_de_downloads_e_revogacao(self):
        d = cvm.ler_detalhe((FIX / "inst409.html").read_text(encoding="utf-8"), "https://x/inst409.html")
        self.assertTrue(d["revogada"])
        self.assertEqual(d["revogada_por"], "Instrução 555/14")
        self.assertEqual(d["data"], "2004-08-18")
        # só os arquivos da própria norma, nunca os PDFs das normas citadas na ementa
        self.assertTrue(d["arquivos"])
        self.assertTrue(all("inst409" in a["url"] for a in d["arquivos"]))
        self.assertIn("sem marcas", d["arquivos"][0]["rotulo"])

    def test_layout_novo_com_links_no_corpo(self):
        d = cvm.ler_detalhe((FIX / "resol251.html").read_text(encoding="utf-8"), "https://x/legislacao/resolucoes/resol251.html")
        self.assertEqual(d["arquivos"][0]["url"].rsplit("/", 1)[-1], "resol251.htm")
        self.assertEqual(d["publicacao"], "Publicada no DOU de 09.11.2026")
        self.assertFalse(d["revogada"])

    def test_cabecalho_yaml(self):
        meta = {"titulo": 'Resolução "X"', "tipo": "Resolução CVM", "numero": "1", "data": "2020-01-01", "ementa": "",
                "revogada": False, "revogada_por": "", "versao_texto": "v", "publicacao": "", "notas": "", "temas": [],
                "fonte": "f", "arquivo": "", "sha256_arquivo": "", "ocr": False, "baixado_em": "2026-11-10"}
        md = cvm.montar_md(meta, "corpo\n")
        self.assertTrue(md.startswith('---\ntitulo: "Resolução \\"X\\""\n'))
        self.assertNotIn("ementa:", md)


class Grafo(unittest.TestCase):
    """Relações lidas dos cabeçalhos reais do acervo (scripts/grafo.py)."""

    @classmethod
    def setUpClass(cls):
        cls.g = grafo.montar(cvm.RAIZ, "cvm", hoje="2026-11-11")
        cls.arestas = {(a["de"], a["para"], a["relacao"]): a for a in cls.g["arestas"]}
        cls.estado = {e["id"]: e for e in cls.g["estado"]}
        cls.externos = {e["id"]: e["url"] for e in cls.g["externos"]}

    def ids(self, texto):
        return [c[0] for c in grafo.citar(grafo.sem_datas(grafo.plano(texto)), "cvm")]

    def test_id_igual_nas_variacoes_de_escrita(self):
        self.assertEqual(self.ids("Instrução 555/14"), ["cvm:instrucao:555"])
        self.assertEqual(self.ids("pelas Instruções 411/04 ; 413/04 e pelas Resoluções 3/20 e 162/22 ."),
                         ["cvm:instrucao:411", "cvm:instrucao:413", "cvm:resolucao:3", "cvm:resolucao:162"])
        self.assertEqual(self.ids("Altera a Deliberação CVM 793/18 ."), ["cvm:deliberacao:793"])
        self.assertEqual(self.ids("VIDE Resolução CMN nº 1.289/87."), ["bcb:resolucao-cmn:1289"])
        self.assertEqual(self.ids("VIDE Lei 8.685/93."), ["lei:8685-1993"])
        self.assertEqual(self.ids("Portaria PTE 132/18"), ["cvm:portaria:132-2018"])  # numeração recomeça todo ano
        self.assertEqual(self.ids("Decisão Conjunta BACEN/CVM 13/03"), ["cvm:decisao-conjunta-bcb:13-2003"])
        self.assertEqual(self.ids("Instrução 480/09 a partir de 1.1.2010"), ["cvm:instrucao:480"])
        self.assertEqual(grafo.desde(grafo.plano("Instrução 480/09 a partir de 1.1.2010")), "2010-01-01")

    def test_instrucao_409_revogada_alterada_e_com_artigo_revogado(self):
        eu = "cvm:instrucao:409"
        self.assertEqual(self.estado[eu], {"id": eu, "caminho": "instrucoes/2004/inst409.md", "estado": "revogada",
                                           "por": ["cvm:instrucao:555"]})
        self.assertEqual(self.arestas[("cvm:instrucao:555", eu, "revoga")]["fonte"], "notas+revogada_por")
        self.assertEqual(sorted(int(k[0].split(":")[2]) for k in self.arestas if k[1] == eu and k[2] == "altera"),
                         [411, 413, 450, 456, 465, 512, 522, 524, 536, 549])
        # 'REVOGADO o art. 74 pela Instrução 522/12' é revogação parcial, não total
        self.assertEqual([k[0] for k in self.arestas if k[1] == eu and k[2] == "revoga_parcial"], ["cvm:instrucao:522"])
        self.assertEqual([k[0] for k in self.arestas if k[1] == eu and k[2] == "revoga"], ["cvm:instrucao:555"])

    def test_norma_conjunta_liga_ao_acervo_do_bcb(self):
        eu = "cvm:decisao-conjunta-bcb:13-2003"
        self.assertEqual(self.estado[eu]["caminho"], "decisoes-conjuntas/2003/dcbccvm13.md")
        self.assertIn((eu, "bcb:decisao-conjunta:13", "conjunta"), self.arestas)
        self.assertEqual(self.externos["bcb:decisao-conjunta:13"],
                         "https://github.com/BrunooMoniz/normas-bcb/blob/main/decisoes-conjuntas/2003/decisao-conjunta-0013.md")
        self.assertEqual(self.estado[eu]["por"], ["cvm:resolucao-conjunta-bcb:11-2024"])
        # a 18/13 da CVM não é a Decisão Conjunta 18 do BCB (de 2010): sem par, e isso fica registrado
        self.assertFalse([k for k in self.arestas if k[0] == "cvm:decisao-conjunta-bcb:18-2013" and k[2] == "conjunta"])
        self.assertTrue([t for t in self.g["trechos"] if t["campo"] == "titulo" and "sem par" in t["padrao"]])

    def test_citacao_de_norma_do_cmn_aponta_para_o_outro_acervo(self):
        self.assertIn(("cvm:instrucao:113", "bcb:resolucao-cmn:1280", "cita"), self.arestas)
        self.assertEqual(self.externos["bcb:resolucao-cmn:1280"],
                         "https://github.com/BrunooMoniz/normas-bcb/blob/main/resolucoes-cmn/1987/resolucao-cmn-1280.md")

    def test_revogacao_com_data(self):
        a = self.arestas[("cvm:instrucao:497", "cvm:instrucao:434", "revoga")]
        self.assertEqual((a["desde"], a["fonte"]), ("2012-01-01", "notas+revogada_por"))

    def test_nada_some_em_silencio(self):
        achaveis = set(self.estado) | set(self.externos) | {x["id"] for x in self.g["nao_resolvidos"]}
        self.assertFalse([a for a in self.g["arestas"] if a["de"] not in achaveis or a["para"] not in achaveis])
        self.assertIn("cvm:portaria:153-2022", {x["id"] for x in self.g["nao_resolvidos"]})  # portaria fora do acervo
        self.assertEqual(len(self.estado), len(list(cvm.RAIZ.glob("[!_.]*/*/*.md"))))  # toda norma tem um id só seu
        self.assertEqual({a["relacao"] for a in self.g["arestas"]} - set(grafo.RELACOES), set())


if __name__ == "__main__":
    unittest.main()
