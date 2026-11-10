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


if __name__ == "__main__":
    unittest.main()
