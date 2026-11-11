# Cobertura

Gerado por `scripts/cvm.py --relatorio`. Índice = itens na busca oficial do portal da CVM.

| Categoria | Índice | Arquivos .md | Com texto | Só metadados | Falhas |
| --- | ---: | ---: | ---: | ---: | ---: |
| Resolução CVM (`resolucoes/`) | 251 | 251 | 251 | 0 | 0 |
| Instrução CVM (`instrucoes/`) | 627 | 627 | 627 | 0 | 0 |
| Deliberação CVM (`deliberacoes/`) | 908 | 908 | 908 | 0 | 0 |
| Parecer de Orientação CVM (`pareceres-de-orientacao/`) | 41 | 41 | 41 | 0 | 0 |
| Ofício-Circular CVM (`oficios-circulares/`) | 601 | 601 | 601 | 0 | 0 |
| Nota Explicativa CVM (`notas-explicativas/`) | 77 | 77 | 77 | 0 | 0 |
| Decisão Conjunta (`decisoes-conjuntas/`) | 34 | 34 | 34 | 0 | 0 |
| Portaria CVM (`portarias/`) | 65 | 65 | 65 | 0 | 0 |
| Portaria Conjunta (`portarias-conjuntas/`) | 2 | 2 | 2 | 0 | 0 |
| **Total** | **2.606** | **2.606** | **2.606** | **0** | **0** |

## Grafo de relações

Gerado por `scripts/grafo.py` a partir dos cabeçalhos, sem IA. Fica em `grafo/`: `arestas.jsonl` (uma relação por linha), `estado.jsonl` (situação de cada norma), `externos.jsonl` (normas do outro acervo e leis do ctresb/leis) e `nao_resolvidos.jsonl`.

| Relação | Arestas | Não resolvidas |
| --- | ---: | ---: |
| revoga | 1.170 | 7 |
| revoga_parcial | 85 | 0 |
| altera | 706 | 17 |
| cita | 891 | 15 |
| regulamenta | 0 | 0 |
| conjunta | 14 | 0 |
| **Total** | **2.866** | **39** (1,4%) |

Não resolvida = aresta que aponta para uma norma sem arquivo neste acervo, no outro ou no ctresb/leis (32 normas distintas). Trechos dos cabeçalhos sem norma reconhecida: 12. Situação calculada: 1.378 vigentes, 65 alteradas e 1.163 revogadas.
