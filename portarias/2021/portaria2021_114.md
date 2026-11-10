---
titulo: "Portaria CVM/PTE Nº 114/2021"
orgao: "Comissão de Valores Mobiliários"
tipo: "Portaria CVM"
numero: "114/2021"
data: 2021-06-25
ementa: "Aprova o novo Plano de Dados Abertos (PDA) da CVM, nos termos do ANEXO A da presente Portaria."
revogada: false
versao_texto: "publicação no portal da CVM"
fonte: "https://conteudo.cvm.gov.br/legislacao/portarias/portaria2021_114.html"
arquivo: "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/portarias/anexos/PortariaPTE2021_114.pdf"
sha256_arquivo: 36ca0eac29affac4cdfe85e02f16e34bc7ad1261ee4229f5e8346a85a9711f2c
baixado_em: 2026-11-10
---
# Portaria CVM/PTE Nº 114/2021

MINISTÉRIO DA ECONOMIA - ME
COMISSÃO DE VALORES MOBILIÁRIOS - CVM

Rua Sete de Setembro, 111 32º andar - Bairro Centro - Rio de Janeiro/RJ - CEP 20050-901
(21)3554-8245 - www.cvm.gov.br

PORTARIA CVM/PTE/Nº 114, DE 25 DE JUNHO DE 2021
O PRESIDENTE DA COMISSÃO DE VALORES MOBILIÁRIOS, no uso das atribuições
que lhe são conferidas pelo Regimento Interno aprovado pela Resolução CVM nº 24, de 5 de março de
2021, resolve:
Art. 1º Aprovar o novo Plano de Dados Abertos (PDA) da CVM, nos termos do ANEXO A
da presente Portaria.
Art. 2º Fica revogada a PORTARIA CVM/PTE/Nº 131, DE 17 DE NOVEMBRO DE 2020.
Art. 3º Esta Portaria entrará em vigor na data da sua publicação.

MARCELO BARBOSA
Presidente

Documento assinado eletronicamente por Marcelo Santos Barbosa, Presidente, em 25/06/2021,
às 17:23, com fundamento no art. 6º do Decreto nº 8.539, de 8 de outubro de 2015.
A autenticidade do documento pode ser conferida no site
https://super.cvm.gov.br/conferir_autenticidade, informando o código verificador 1292287 e o código
CRC CDFC57A5.
This document's authenticity can be verified by accessing https://super.cvm.gov.br/conferir_autenticidade, and
typing the "Código Verificador" 1292287 and the "Código CRC" CDFC57A5.

ANEXO A DA PORTARIA CVM/PTE/Nº 114, DE 25 DE JUNHO DE 2021

Plano de Dados Abertos
COMISSÃO DE VALORES MOBILIÁRIOS

Mês/ano início: junho/2021
Mês/ano término: junho/2023

SUMÁRIO
1. INTRODUÇÃO ......................................................................................................................... 3
2. CENÁRIO INSTITUCIONAL................................................................................................. 4
3. OBJETIVOS .............................................................................................................................. 5
3.1. Objetivo geral ....................................................................................................................... 5
3.2. Objetivos específicos............................................................................................................ 5
4. CONSTRUÇÃO E EXECUÇÃO DO PLANO DE DADOS ABERTOS.............................. 5
5. DADOS SELECIONADOS PARA ABERTURA ................................................................... 6
6. O PROCESSO DE CATALOGAÇÃO .................................................................................... 6
7. SUSTENTAÇÃO, MONITORAMENTO E CONTROLE.................................................... 6
8. PLANO DE AÇÃO.................................................................................................................... 8
8.1. Cronograma de elaboração e sustentação do PDA ............................................................... 8
8.2. Cronograma de abertura de bases ......................................................................................... 9
8.3. Cronograma de promoção, fomento, uso e reuso das bases ............................................... 11
ANEXOS ...................................................................................................................................... 12
A - Inventário de bases de dados da CVM ................................................................................ 12
B - Diretrizes gerais................................................................................................................... 14
C - Estratégias para abertura....................................................................................................... 15
Referências ................................................................................................................................... 16
Glossário....................................................................................................................................... 17
NOTAS ......................................................................................................................................... 18

2

1. INTRODUÇÃO
A CVM, por meio do presente documento, apresenta o seu Plano de Dados Abertos (PDA),
o qual orientará as atividades desta Autarquia para abertura, manutenção, monitoramento
e fomento ao uso de suas bases de dados até janeiro de 2023. O PDA visa orientar as ações de
implementação e promoção da abertura dos dados da Autarquia, facilitando o acesso e a
utilização, pelo cidadão, das informações detidas pela CVM, bem como seu intercâmbio com
outros órgãos e entidades públicas. Neste sentido, o plano abrange quaisquer dados gerados
pela Autarquia ou por ela recebidos no exercício de suas atribuições legais, desde que não estejam
sob sigilo ou tenham alguma outra restrição de acesso.
Cabe salientar que o primeiro PDA-CVM foi lançado em 2016, por meio da Portaria
CVM/PTE/nº 180, de 15/12/2016, com pleno alinhamento à Política de Dados Abertos do
Poder Executivo Federal, instituída pelo Decreto nº 8.777, de 11 de maio de 2016, que visa, entre
outros objetivos, aprimorar a cultura de transparência pública, franqueando ao cidadão

o

acesso, de forma aberta, aos dados produzidos ou acumulados pela Administração
Pública1¹. Desde então, a Comissão tem ampliado sua transparência ativa e as bases de dados
que estão disponíveis ao cidadão em seu portal de dados abertos (http://dados.cvm.gov.br/).
O presente plano também considera os princípios e diretrizes estabelecidos

pela

Resolução nº 3, de 13 de outubro de 2017, do Comitê Gestor da Infraestrutura Nacional de
Dados Abertos (CGINDA)² , que aprovou normas sobre a elaboração e publicação de Planos de
Dados Abertos; a Instrução Normativa STL nº 4, de 13 de abril de 2012, que criou a
Infraestrutura Nacional de Dados Abertos (INDA)³ , a Política Nacional de Governo
Aberto (Decreto nº 10.160, de 09 de dezembro de 2019), além dos parâmetros estabelecidos na
arquitetura de interoperabilidade do governo eletrônico e os vocabulários e ontologias de Governo
Eletrônico.
Deve ser salientado que o PDA-CVM não se aplica apenas aos dados gerados pela
Autarquia, mas também àquelas informações recebidas de participantes do mercado de
capitais,

encaminhadas

de

forma

voluntária

ou

em

atenção

à

legislação

ou

regulamentação aplicável. Nesse sentido, cabe destacar que a própria lei que instituiu a CVM
exige que o exercício das atribuições da Autarquia deve perseguir algumas finalidades
(art. 4º, Lei nº 6.385, de 7 de dezembro de 1976), entre elas a de "assegurar o acesso do
público a informações sobre os valores mobiliários negociados e as companhias que os
tenham emitido". Essa é uma questão sensível, pois muitos dados de terceiros envolvem
informações pessoais, sendo especialmente aplicáveis as regras da Lei Geral de Proteção de Dados
(LGPD), a Lei nº 13.709, de 14 de agosto de 2018, que entrou em vigor em 2020.
Assim, ao longo de sua história, a Autarquia sempre exigiu que os participantes de
mercado encaminhassem informações periódicas e eventuais. Esse acervo documental, aliado
àquele que foi produzido pela própria CVM no exercício de suas atribuições, contém um
registro importante, e muitas vezes único, das atividades exercidas pela Comissão em mais
3

de 40 anos de existência, o qual observa, cumpre salientar, as diretrizes e regras da política
nacional de arquivos públicos e privados (Lei nº 8.159, de 3 de janeiro de 2002). Evidentemente,
nem todas as informações são destinadas à guarda permanente, sendo algumas eliminadas
segundo a regulamentação aplicável em cada momento.

2. CENÁRIO INSTITUCIONAL
A elaboração desta nova edição do PDA-CVM considerou os valores, as prioridades e os
objetivos estabelecidos pelo Planejamento Estratégico da CVM (“Construindo a CVM de
2023”).4
O documento foi elaborado por meio de processo de construção coletiva que confirmou e
atualizou os valores da CVM, cabendo destacar os seguintes, por sua pertinência com o tema
desta publicação:
- “Atuação pautada na proteção do investidor, na exigência de ampla divulgação de
informação, no monitoramento dos riscos de mercado e na estabilidade financeira,
inclusive com o apoio da autorregulação”;
- “Atuação regulatória com foco no atendimento das necessidades do mercado e sua
evolução, em consonância com padrões internacionais, e pautada na participação da
sociedade, inclusive por meio de audiências públicas”; e
- “Busca permanente de estruturas organizacional, física e tecnológica adequadas,
suportadas por uma autonomia administrativa, orçamentária e financeira”.
Outros documentos importantes, do ponto de vista do cenário institucional de elaboração do
PDA-CVM, são a Política de Governança de Tecnologia da Informação (PGTI), em especial a
governança de dados por ela estabelecida, e o Plano Diretor de Tecnologia da Informação
(PDTI) da Autarquia, que é atualizado anualmente. Como instrumento de diagnóstico,
planejamento e gestão,

o PDTI alinha os investimentos em TI ao planejamento

estratégico da Autarquia, orientando o processo de tomada de decisão. Entre as diretrizes que
orientam o plano está a prioridade a ser dada à adoção de padrões abertos no desenvolvimento
de tecnologia da informação e comunicação. Cabe destacar que sua concepção e monitoramento
são conduzidos por um comitê específico, o Comitê de Governança de Tecnologia da Informação
e Transformação Digital – CGTI, instituído pela Portaria CVM/PTE/Nº 197, de 22 de novembro
de 20195.
Finalmente, em linha com a Política Nacional de Arquivos, a CVM editou em 2017 a sua Política
de Gestão de Documentos, que busca assegurar o direito fundamental de acesso à informação,
promovendo a transparência da gestão, por meio da organização e preservação do acervo
de documentos e processos, independentemente do suporte.

4

3. OBJETIVOS
3.1. OBJETIVO GERAL
Promover a abertura de dados na CVM, zelando pelos princípios da publicidade,
transparência e eficiência, segundo as diretrizes a seguir mencionadas:
- expansão do número de bases de dados abertas (quantidade de dados);
- melhoria da qualidade dos dados disponibilizados, de forma a contribuir para a tomada de
decisão pelos gestores públicos e incentivar o controle social (qualidade dos dados); e
- compromisso com a progressiva ampliação do compartilhamento de dados com outros órgãos
da administração pública federal, nos termos do Decreto nº 10.046, de 9 de outubro de 20196.
3.2. OBJETIVOS ESPECÍFICOS
Os seguintes objetivos específicos deverão ser alcançados pela implementação do
presente PDA:

• Identificar e priorizar a abertura de dados com grau de relevância para o cidadão;
• Estimular o controle social;
• Fornecer dados atualizados e os respectivos históricos, melhorando a qualidade dos dados
disponibilizados;

• Apoiar a pesquisa e estudos técnicos e acadêmicos, contribuindo para a produção de
conhecimento no âmbito do mercado de valores mobiliários;

• Incrementar os processos de transparência ativa; e
• Fomentar propostas de inovação e de desenvolvimento tecnológico e sustentável.

4. CONSTRUÇÃO E EXECUÇÃO DO PLANO DE DADOS ABERTOS
Esta nova edição do PDA-CVM considerou os valores, as prioridades e os objetivos
estabelecidos pelo Planejamento Estratégico da CVM, conforme discriminado em maiores
detalhes no item 2.
Assim, a Assessoria de Análise e Pesquisa (ASA) e a Superintendência de Tecnologia da
Informação (STI) e a Superintendência de Proteção e Orientação aos Investidores (SOI) atuaram
de forma colaborativa para mapear todas as bases de dados existentes na CVM, de modo a
avaliar quais deveriam ser abertas, levando em consideração as demandas do público e as
exigências de transparência ativa. A Superintendência de Tecnologia da Informação (STI)
avaliou a viabilidade tecnológica da abertura, enquanto cada componente organizacional
responsável pelo preparo e atualização dos dados avaliou a viabilidade operacional.
Demandas do cidadão e pesquisas junto ao público foram também consideradas como insumos
para a elaboração do presente PDA.
Assim, após criteriosa avaliação da ASA, SOI, STI e de cada componente gerador dos dados, sob
a coordenação da Superintendência Geral (SGE), a CVM elaborou o atual Plano de Dados
Abertos, a ser revisado periodicamente.
5

5. DADOS SELECIONADOS PARA ABERTURA

Os dados selecionados para a abertura e a sua priorização terão por base pesquisa realizada junto
aos usuários das nossas informações quantitativas. Esse trabalho encontra-se reunido no
documento intitulado como “Percepção dos usuários sobre a plataforma e os dados quantitativos
disponibilizados pela CVM”.
Buscamos identificar as informações mais consumidas pelo público em geral, divididos em cinco
categorias: Academia, Institucional, Setor Privado, Pessoa Física e Setor Público. O trabalho
ainda tratou de possíveis pontos de melhorias na disponibilização e captura de informações
quantitativas, que estão sendo levados em conta em diversos projetos internos, como a
reformulação do Boletim de Mercado e Risco da CVM e o próprio site da Autarquia.
Link para a pesquisa:
http://conteudo.cvm.gov.br/export/sites/cvm/noticias/anexos/2020/20200601_resultado_pesquisa
_cvm_percepcao_usuarios_plataforma_e_dados.pdf

6. O PROCESSO DE CATALOGAÇÃO
A catalogação dos dados no Portal Brasileiro de Dados Abertos será de responsabilidade de cada
uma

das

Superintendências

responsáveis

pelos

dados,

sob

a

coordenação

da

Superintendência de Tecnologia da Informação da CVM (STI). Sempre que possível, essa
atividade será realizada de forma automatizada, observando-se as informações prestadas pela
Superintendência responsável, cabendo à STI o controle das estatísticas de publicação e
atualização das referidas bases de dados.

7. SUSTENTAÇÃO, MONITORAMENTO E CONTROLE
Os componentes organizacionais da CVM que geraram as informações ou que têm
responsabilidade pela sua requisição aos participantes de mercado são os responsáveis por
verificar a acurácia e qualidade das informações nos metadados respectivos. A curadoria
da publicação dos dados será de responsabilidade da ASA, SOI e STI, sob a coordenação do
SGE, cabendo-lhes propor melhorias nos processos de abertura de dados e nas bases abertas,
tanto do ponto de vista quantitativo quanto qualitativo.
Sem prejuízo dessa atuação conjunta pela melhoria da qualidade e expansão das bases de dados
abertas pela CVM, competirá a cada um dos componentes organizacionais abaixo mencionados
as seguintes responsabilidades específicas:
- ASA - identificar e propor melhoria na qualidade dos dados abertos;
- SOI - monitorar a disponibilidade dos arquivos catalogados; e

6

- STI - verificar se os padrões da INDA e INDE (metadados atualizados contendo a
descrição,

contatos

dos

responsáveis

pelas

informações

e

dos

outros

metadados

associados a cada conjunto de dados) estão sendo observados.
O PDA-CVM será acompanhado e monitorado pelo SGE, com o apoio da ASA, SOI e STI. A
SOI será responsável pela disponibilização do PDA ao cidadão, cabendo-lhe também:
- receber, processar e responder a sugestões, consultas e reclamações do público externo no que
se refere ao PDA-CVM ou aos dados abertos pela CVM, por meio do SAC (Serviço de
Atendimento ao Cidadão), do e-SIC (Serviço de Informação ao Cidadão) ou de outro canal
disponível ao cidadão;
- atualizar a Carta de Serviços ao Usuário para fazê-la refletir o PDA-CVM;
- orientar os serviços de atendimento ao público no sentido de esclarecerem dúvidas e
prestarem orientações quanto ao acesso aos dados, bem como sobre os procedimentos para
requerer a abertura de uma base de dados; e
- fazer levantamentos junto aos investidores e ao cidadão quanto a interesse na abertura
de dados, construindo mecanismos de participação social para aprimoramento do PDACVM.

7

8. PLANO DE AÇÃO
Esta seção detalha as atividades e responsabilidades relacionadas ao processo de publicação de dados, incluindo prazos e requisitos.
8.1. CRONOGRAMA DE ELABORAÇÃO E SUSTENTAÇÃO DO PDA
Id. Ação
Atividades
1
Planejar a abertura das bases de dados Estabelecer cronograma de ações
selecionadas na lista priorizada
necessárias para a publicação em
formato
aberto
das
bases
selecionadas, conforme a lista
priorizada.
2
Divulgar a lista de bases de dados
Elaborar plano de comunicação
para a divulgação da abertura das
bases de dados selecionadas na
lista priorizada do PDA.

Objetivo
Responsáveis
Prazo
Definir, com as unidades, as ações
ASA, STI
DEZ/20
necessárias para a abertura das
bases de dados selecionadas na
lista priorizada e estabelecer os
respectivos cronogramas.
Definir ações de comunicação
ASC
DEZ/20-JAN/21
necessárias
para
dar
ampla
publicidade à divulgação da
abertura das bases de dados
selecionadas na lista priorizada do
PDA.
3
Realizar a abertura das bases de Executar as ações necessárias para Disponibilizar para a sociedade, em STI
JAN/21 – DEZ/23
dados selecionadas
a publicação em formato aberto
formato aberto no portal de
das bases selecionadas na lista dados da CVM, as bases
priorizada do PDA, conforme
selecionadas na lista priorizada do
cronograma estabelecido.
PDA.
4
Planejar nova abertura de bases de Revisão do PDA
Promover a atualização do PDA.
ASA, STI
SET-OUT/23
dados
5
Atualização do PDA e divulgação da Revisão do PDA
Promover a atualização do PDA.
ASA, SOI, STI, ASC
DEZ/23-JAN/24
lista de bases de dados
6
Realizar a abertura das novas bases Executar as ações necessárias para Disponibilizar para a sociedade, em STI
JAN/24 – DEZ/26
de dados selecionadas
a publicação em formato aberto
formato aberto no portal de
Das novas bases selecionadas
dados da CVM
7
Elaboração do PDA 2023-2025
SGE, ASA, SOI, STI
DEZ/23
Este plano não inclui as ações e respectivas atividades já iniciadas, em especial a disponibilização das bases de dados definidas anteriormente, sob a
responsabilidade da ASA e STI. Também não inclui as atividades necessárias à definição da lista de bases de dados a serem publicadas em formato aberto ao longo
de 2021, a partir da interlocução com os diferentes componentes organizacionais (ASA e STI) e pesquisas junto a investidores e ao público em geral (SOI).

8

8.2. CRONOGRAMA DE ABERTURA DE BASES

Nome da base de dados

Conjunto de dados

Documentos Periódicos e Companhias: Documentos periódicos e
Eventuais de Regulados eventuais do IPE

Descrição da base / conjunto de dados
Documentos não estruturados entregues
pelas companhias

Unidade e contato do
responsável pela base/
conjunto de dados

Frequência de Meta/ Prazo
atualização
para abertura

SEP

Semanal

30/06/2021

SSE

Diária

30/06/2021

SRE

Diária

30/06/2021

Documentos Periódicos e Companhias: Demonstração de Resultado Demonstrações financeiras entregues pelas
Eventuais de Regulados Abrangente (ITR/DRA)
companhias

SEP

Semanal

30/06/2021

Documentos Periódicos e Companhias: Demonstração de Resultado Demonstrações financeiras entregues pelas
Eventuais de Regulados Abrangente (DFP/DRA)
companhias

SEP

Semanal

30/06/2021

SSE

Diária

30/06/2021

SSE

Semanal

30/09/2021

SSE

Semanal

30/09/2021

SSE

Semanal

30/09/2021

SSE

Semanal

31/03/2022

SIN

Semanal

30/06/2022

Cadastro de Regulados
Cadastro de Regulados

Cadastro de Regulados

Agentes Fiduciários: Informações
cadastrais
Emissores CEPAC: Informações
cadastrais

Plataformas de Crowdfunding:
Informações cadastrais

Informações cadastrais de agentes
fiduciários
Informações cadastrais de emissores de
CEPAC

Informações cadastrais de plataformas de
crowdfunding

Documentos Periódicos e
FII: Informe Mensal
Eventuais de Regulados
Documentos Periódicos e
FII: Informe Trimestral
Eventuais de Regulados
Documentos Periódicos e
FII: Informe Anual
Eventuais de Regulados
Documentos Periódicos e
FII: Demonstrações Financeiras
Eventuais de Regulados

Informes entregues pelos fundos de
investimento imobiliário
Informes entregues pelos fundos de
investimento imobiliário
Informes entregues pelos fundos de
investimento imobiliário
Documentos entregues pelos fundos de
investimento imobiliário

Documentos Periódicos e
FIP: Balanço Analítico Semestral
Eventuais de Regulados

Conteúdo estruturado do balanço de fundos
de investimento em participações

9

Documentos Periódicos e Companhias Securitizadoras: Informe
Eventuais de Regulados Mensal de CRI
Documentos Periódicos e Companhias Securitizadoras: Informe
Eventuais de Regulados Mensal de CRA

Conteúdo estruturado do informe mensal de
securitizadora, referente a Certificados de
Recebíveis Imobiliários
Conteúdo estruturado do informe mensal de
securitizadora, referente a Certificados de
Recebíveis Agropecuários

SSE

Semanal

31/12/2022

SSE

Semanal

31/12/2022

Documentos Periódicos e Companhias: Informe do Código de
Eventuais de Regulados Governança

Conteúdo estruturado do informe do código
de governança, entregue pelas companhias

SEP

Semanal

30/06/2023

Documentos Periódicos e Companhias: Valores Mobiliários
Eventuais de Regulados Negociados e Detidos

Conteúdo estruturado do informe de valores
mobiliários negociados e detidos (art. 11 da
Instr. CVM nº 358)

SEP

Semanal

30/06/2023

Documentos Periódicos e Companhias Securitizadoras:
Eventuais de Regulados Demonstrações Financeiras de CRI

Demonstrações contábeis do patrimônio
separado de CRI

SSE

Semanal

31/12/2023

Documentos Periódicos e Companhias Securitizadoras:
Eventuais de Regulados Demonstrações Financeiras de CRA

Demonstrações contábeis do patrimônio
separado de CRA

SSE

Semanal

31/12/2023

10

8.3. CRONOGRAMA DE PROMOÇÃO, FOMENTO, USO E REUSO DAS BASES

Produto

Atividades

Unidade e contato do
Responsável

1.
Publicação
de
matérias Publicar matérias, no site da CVM e chamadas nas
informando sobre a publicação de redes sociais institucionais, em meses de
bases e o seu conteúdo.
publicação de bases
ASC

Data/período

Mês corrente ou subsequente à
abertura de nova base

2. Consolidação de conhecimento

Publicar matéria anual, no site da CVM e
chamadas nas redes sociais institucionais,
consolidando a atividade anual de abertura de
dados
ASC/ASA/STI

1º trimestre 2022

3. Consolidação de conhecimento

Publicar matéria anual, no site da CVM e
chamadas nas redes sociais institucionais,
consolidando a atividade anual de abertura de
dados
ASC/ASA/STI

1º trimestre 2023

11

ANEXO
A - INVENTÁRIO DE BASES DE DADOS DA CVM

Descrição da base

Unidade(s)
responsável(is)
pela base

Disponível em
dados.gov.br?

Periodicidade de
atualização

Cadastro de
Regulados
Documentos
Periódicos e
Eventuais de
Regulados

Informações cadastrais de participantes de
mercado

SIN, SEP, SMI,
SRE, SNC, SSE

Parcialmente

Diária

Sim

Informes e documentos entregues à CVM
por participantes de mercado

SIN, SEP, SMI,
SNC, SSE, SOI

Parcialmente

Semanal

Sim

Ofertas Públicas de
Distribuição

Informações sobre ofertas de valores
mobiliários, emissores e ofertantes

SRE

Parcialmente

Diária

Sim

Nome da base de
dados

Operações/
Negociações
Processos e
Documentos
Administrativos

Atos Declaratórios
Desvios e
Performance de
Auditores
Independentes

Política pública Possui conteúdo sigiloso
relacionada,
ou alguma outra
restrição de acesso?
quando aplicável

Informações sobre investidores, emissores,
fundos de investimento, intermediários,
fatos relevantes, ordens, negócios, posições,
cotações de ativos
Informações sobre processos
administrativos, andamentos, documentos,
processos sancionadores, acusados,
investigados, decisões, penalidades
Registro da existência ou não de autorização
da CVM para que determinada pessoa
exerça a atividade de intermediação de
valores mobiliários

SMI

Não

Sim

DINF/SOI, SPS,
SSR, SEP

Não

Sim

SIN, SMI, SNC

Não

Não

Informações sobre desvios e performances
de auditores independentes

SNC

Não

Sim

12

Consultas,
Reclamações e
Denúncias de
Investidores

Informações do Serviço de Atendimento ao
Cidadão (SAC) da CVM: consultas,
reclamações, sugestões, denúncias

GOI-1/SOI

Não

Sim

Audiência a
Particulares

Informações sobre audiências de cidadãos
junto aos setores da CVM

STI

Não

Sim

Arrecadação

Informações sobre multas, taxas, débitos

GEARC/SAD,
PFE

Não

Sim

Recursos Humanos

Informações sobre servidores, histórico
funcional, movimentações, afastamentos,
frequência, planos de metas, avaliações de
desempenho, pontuações por desempenho,
ofertas de benefícios

GEGEP/SAD,
DICAD/SAD

Não

Sim

Demandas de TI

Informações sobre demandas de TI, ordens
de serviço, contratos, prestadores de serviço,
serviços, incidentes, problemas, dúvidas

STI

Não

Sim

Patrimônio

Informações sobre tombos, bens móveis,
ordens de serviço

GEMAP/SAD

Não

Não

Administração

Informações sobre gastos com serviços de
reprografia, telefonia e garagem

GEMAP/SAD

Não

Não

Portal Institucional

Legislação, decisões do colegiado, contratos,
licitações, institucional, noticias,
informações sobre participantes de mercado

ASC

Não

Não

13

B - DIRETRIZES GERAIS
Abrangem os fundamentos e critérios para seleção dos dados a serem abertos. Os
seguintes critérios são considerados pela CVM, desde o primeiro PDA:

• Origem dos dados: A CVM, no exercício de suas atribuições, recebe e processa dados de
diferentes fontes: órgãos e entidades públicas, provedores de serviços de informações,
participantes

de

mercado

(cumprindo

obrigações

estabelecidas

pela

legislação

e

regulamentação de mercado). Esse conjunto de informações é heterogêneo e apenas a
análise caso a caso pode indicar o melhor procedimento, todavia, como procedimento geral,
entende-se que os dados fornecidos por participantes supervisionados pela CVM, salvo
exceções previstas estabelecidas na legislação aplicável, são os mais vocacionados para
disponibilização em formato aberto, com respectiva publicação no Portal Brasileiro de Dados
Abertos (http://dados.gov.br/).

• Demanda

pela

informação:

A

disponibilização

pública

de

dados

está

em

consonância com a atribuição legal da Autarquia de proteger investidores que operam no
mercado de valores mobiliários. Um dos fatores cruciais para esse objetivo é o provimento
de informações para que os investidores possam tomar decisões informadas e acompanhar os
seus investimentos, lidando dessa forma com problemas decorrentes de assimetria de
informações, que incluem questões relacionadas à seleção adversa e ao risco moral.

• Informações públicas: Parte substancial das informações encaminhadas à CVM por
participantes de mercado já está disponível na página da Autarquia na Internet, embora, em alguns
casos, sem dados históricos. Como diretriz geral, devem ser abertos e disponibilizados todos os
dados de domínio público.

• Formato na recepção: A CVM requer dos administradores das companhias abertas e
dos fundos de investimentos um conjunto bastante abrangente de informações e dados.
Nesse sentido, diversos formatos são utilizados no envio dos documentos, dependendo do
conteúdo das informações. Algumas informações, por exemplo, são encaminhadas de forma
eletrônica, em formato .PDF, outras, por sua vez, são enviadas em formato texto, em
campos

de

formulários específicos,

havendo

ainda

aquelas

fornecidas

de

forma

estruturada, de fácil agregação ou consolidação. Por fim, há ainda documentos que
combinam informações estruturadas com outras em forma de texto livre. Como critério, será
priorizada a abertura de dados estruturados, pela facilidade futura de manuseio direto pelos
usuários, sem prejuízo da possibilidade de envio de informações na forma de texto livre.
•

Questões de ordem tecnológica e de qualidade: Há a necessidade de avaliação detalhada

sobre a viabilidade de publicação no Portal de Dados Abertos de cada série histórica de dados,
tanto em termos tecnológicos quanto em termos de qualidade dessas informações.

Nesse

sentido, há priorização para dados que decorram de exigências normativas em vigor há pelo
menos 2 anos. Esse critério visa assegurar a qualidade da informação, pois há uma
14

natural curva de aprendizagem por parte das entidades reguladas pela CVM, toda vez que
nova obrigação informacional é instituída.


Identificação dos dados a serem abertos conforme as diretrizes gerais:

Seguindo os critérios acima, e a partir da revisão do plano de ação anterior, foi elaborada uma
nova lista de documentos para abertura em 2020. Esse conjunto de informações abrange as
ofertas públicas de distribuição, além dos dados cadastrais dos seguintes participantes de
mercado:

• Administradores de Carteira
• Administradores de Fundos Imobiliários
• Agentes Autônomos
• Auditores
• Cias Estrangeiras
• Cias Incentivadas
• Consultores de Valores Mobiliários
• Representantes de Investidores Não Residentes
Os dados a serem abertos em 2021 serão definidos e disponibilizados conforme
cronograma estabelecido neste PDA.

C - ESTRATÉGIAS PARA ABERTURA
Sob a coordenação do Superintendente Geral, a Assessoria de Análise e Pesquisa (ASA), a
Superintendência de Proteção e Orientação aos Investidores (SOI) e a Superintendência de
Tecnologia da Informação (STI) deverão, a cada dois anos, reavaliar o conjunto de dados que
poderá ser aberto. A decisão final pela abertura levará em consideração os critérios de
priorização definidos pela ASA e pela SOI, neste caso considerando as demandas do
público e as exigências de transparência ativa. Avaliada a viabilidade tecnológica da
abertura, pela STI, e operacional, junto ao componente organizacional responsável pelo
preparo e atualização dos dados, será elaborada proposta de abertura. O PDA-CVM também será
revisado periodicamente.

15

REFERÊNCIAS
1) Lei Complementar nº 101, de 4 de maio de 2001, determinando ao Poder Público a adoção de
instrumentos de transparência na gestão fiscal em meios eletrônicos de acesso público às
informações orçamentárias e prestações de contas;

2) Infraestrutura Nacional de Dados Abertos – INDA:
- Instrução Normativa nº 4, de 13 de abril de 2012, que cria a INDA e estabelece os seguintes
conceitos: dado, informação, dado público, formato aberto, licença aberta, dados abertos e
metadado;
- O Plano de Ação da INDA, que institui a necessidade de os órgãos de instituírem seus
respectivos Planos de Abertura de Dados com vistas a uma Política Nacional de Dados
Abertos e institui os elementos mínimos do documento, bem como orienta que a abertura
de dados deve observar a relevância para o cidadão;

3) Política Nacional de Governo Aberto;
4) Lei nº 12.527, de 18 de Novembro de 2011 (Lei de Acesso à Informação - LAI);
5) Padrões de Interoperabilidade de Governo Eletrônico, chamados e-PING;
6) Vocabulários e Ontologias do Governo Eletrônico - e-VoG;
7) Modelo de Acessibilidade de Governo Eletrônico - e-MAG;
8) Planejamento Estratégico 2013-2023 e o PDTI da CVM.

16

GLOSSÁRIO
Dado - sequência de símbolos ou valores, representados em qualquer meio, produzidos como
resultado de um processo natural ou artificial;
Dado acessível ao público - qualquer dado gerado ou acumulado pelo Governo que não esteja
sob sigilo ou sob restrição de acesso nos termos da Lei nº 12.527, de 18 de 4 novembro de
2011;
Dados abertos - dados acessíveis ao público, representados em meio digital, estruturados em
formato aberto, processáveis por máquina, referenciados na internet, disponibilizados, sob licença
aberta ou sob domínio público que permita sua livre utilização, consumo ou cruzamento,
limitando-se a creditar a autoria ou a fonte;
Dados Abertos Governamentais - metodologia para a publicação de dados do governo em
formatos reutilizáveis, visando o aumento da transparência e maior participação política
por

parte

do

cidadão,

além

de

gerar

diversas

aplicações

desenvolvidas

colaborativamente pela sociedade;

Formato aberto - formato de arquivo não proprietário, cuja especificação esteja
documentada publicamente e seja de livre conhecimento e implementação, livre de
patentes ou qualquer outra restrição legal quanto à sua utilização;

Governança Digital - utilização, pelo setor público, de tecnologias da informação e
comunicação com o objetivo de melhorar a informação e a prestação de serviços,
incentivando a participação dos cidadãos no processo de tomada de decisão e tornando o
governo mais responsável, transparente e eficaz; e
Plano de Dados Abertos - documento orientador para as ações, com prazos definidos, de
implementação e promoção de abertura de dados de cada órgão ou entidade da
administração pública federal, obedecidos os padrões mínimos de qualidade, de forma a facilitar
o entendimento e a reutilização das informações.

17

NOTAS
¹O Plano de Ação para 2017 (anexo I), contido na primeira versão desde documento, foi
plenamente executado e culminou na abertura de 100% dos dados selecionados pela CVM no
Portal de Dados Abertos do Governo Federal.
² https://wiki.dados.gov.br/GetFile.aspx?File=%2fComiteGestor%2fResolu%c3%a7%c3%b5es%
2fresolucao-cginda-2-24-3-2017%2cpdf.pdf
³https://dados.gov.br/pagina/instrucao-normativa-da-inda
4

http://www.cvm.gov.br/menu/acesso_informacao/planos/estrategico/estrategico.html

5

http://www.cvm.gov.br/export/sites/cvm/menu/acesso_informacao/institucional/comites/portari
a_cvm_pte_197_2019_comites.pdf
6

http://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2019/Decreto/D10046.htm

7

A Infraestrutura Nacional de Dados Abertos (INDA) é um conjunto de padrões, tecnologias,
procedimentos e mecanismos de controle necessários para atender às condições de disseminação
e compartilhamento de dados e informações públicas no modelo de Dados Abertos. A INDA é a
política do governo brasileiro para dados abertos.
8

http://wiki.gtinda.ibge.gov.br/Plano-de-Acao-da-INDA.ashx

9

https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10160.htm

10

http://eping.governoeletronico.gov.br/

11

http://vocab.e.gov.br/

12

http://emag.governoeletronico.gov.br/

18
