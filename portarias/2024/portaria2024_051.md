---
titulo: "Portaria CVM/PTE Nº 51/2024 (Revogada)"
orgao: "Comissão de Valores Mobiliários"
tipo: "Portaria CVM"
numero: "51/2024"
data: 2024-05-23
ementa: "Aprova o novo Plano de Dados Abertos (PDA) da CVM, nos termos do ANEXO A da presente Portaria."
revogada: true
revogada_por: "Portaria PTE 176/2026"
versao_texto: "publicação no portal da CVM"
notas: "REVOGADA pela Portaria PTE 176/2026 ."
fonte: "https://conteudo.cvm.gov.br/legislacao/portarias/Portaria2024_051.html"
arquivo: "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/portarias/anexos/PortariaPTE2024_051.pdf"
sha256_arquivo: b8067cd69badf427cbe52ea7e869d893eb69f27db296d624e4eeefdffa9eccf2
baixado_em: 2026-11-10
---
# Portaria CVM/PTE Nº 51/2024 (Revogada)

MINISTÉRIO DA ECONOMIA - ME
COMISSÃO DE VALORES MOBILIÁRIOS - CVM
Rua Sete de Setembro, 111 32º andar - Bairro Centro - Rio de Janeiro/RJ - CEP 20050-901
(21)3554-8245 - www.cvm.gov.br

PORTARIA CVM/PTE/Nº 51, DE 23 DE MAIO DE 2024
O PRESIDENTE DA COMISSÃO DE VALORES MOBILIÁRIOS, no uso
das atribuições que lhe são conferidas pelo Regimento Interno da CVM, aprovado
pela Resolução CVM nº 24, de 5 de março de 2021, resolve:
Art. 1º Aprovar o novo Plano de Dados Abertos (PDA) da CVM, nos
termos do ANEXO A da presente Portaria.
Art. 2º Revogar a PORTARIA CVM/PTE/Nº 182, de 20 de dezembro de
2023.
Art. 3º Esta Portaria entrará em vigor 3 de junho de 2024.

JOÃO PEDRO BARROSO DO NASCIMENTO
Presidente

Documento assinado eletronicamente por João Pedro Barroso do
Nascimento, Presidente, em 23/05/2024, às 09:50, com fundamento no art.
6º do Decreto nº 8.539, de 8 de outubro de 2015.
A autenticidade do documento pode ser conferida no site
https://sei.cvm.gov.br/conferir_autenticidade, informando o código verificador
2042267 e o código CRC D48FC5C9.
This document's authenticity can be verified by accessing
https://sei.cvm.gov.br/conferir_autenticidade, and typing the "Código Verificador"
2042267 and the "Código CRC" D48FC5C9.

Portaria CVM/PTE 51 (2042267)

SEI 19957.015409/2023-54 / pg. 1

ANEXO A DA PORTARIA CVM/PTE/N° 51, DE 23 DE MAIO DE 2024

Plano de Dados Abertos

COMISSÃO DE VALORES MOBILIÁRIOS

Mês/ano início: junho/2024

Mês/ano término: maio/2026

Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 2

Sumário
1.

INTRODUÇÃO .......................................................................................................................... 3

2.

CENÁRIO INSTITUCIONAL ................................................................................................... 4

3.

OBJETIVOS ............................................................................................................................... 5
3.1.

OBJETIVO GERAL......................................................................................................... 5

3.2.

OBJETIVOS ESPECÍFICOS ............................................................................................ 5

4.

CONSTRUÇÃO E EXECUÇÃO DO PLANO DE DADOS ABERTOS................................... 6

5.

DADOS SELECIONADOS PARA A ABERTURA .................................................................. 6

6.

O PROCESSO DE CATALOGAÇÃO ....................................................................................... 9

7.

SUSTENTAÇÃO, MONITORAMENTO E CONTROLE......................................................... 9

8.

PLANO DE AÇÃO ................................................................................................................... 11
8.1.

CRONOGRAMA DE ELABORACÃO E SUSTENTAÇÃO DO PDA .................. 11

8.2.

CRONOGRAMA DE ABERTURA DE BASES – 2024 e 2025 .............................. 12

8.3.

CRONOGRAMA DE PROMOÇÃO, FOMENTO, USO E REUSO DAS BASES .13

ANEXOS ................................................................................................................................... 14

A - INVENTÁRIO DE BASES DE DADOS DA CVM ............................................................. 14
B - DIRETRIZES GERAIS .......................................................................................................... 19
C - ESTRATÉGIAS PARA ABERTURA .................................................................................... 20
REFERÊNCIAS ................................................................................................................................ 21
GLOSSÁRIO .................................................................................................................................... 22
NOTAS ............................................................................................................................................. 23

2

Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 3

1. INTRODUÇÃO
A CVM, por meio do presente documento, apresenta o seu mais recente Plano de Dados
Abertos (PDA), o qual orientará as atividades desta Autarquia para abertura, manutenção,
monitoramento e fomento ao uso de suas bases de dados até abril de 2026. O PDA visa
orientar as ações de irnplementação e promoção da abertura dos dados da Autarquia,
facilitando o acesso e a utilização, pelo cidadão, das informações detidas pela CVM, bem
como seu intercâmbio com outros órgãos e entidades públicas. Neste sentido,o plano
abrange quaisquer dados gerados pela Autarquia ou por ela recebidos no exercício de suas
atribuições legais, desde que não estejam sob sigilo ou tenham alguma outra restrição de
acesso.
Cabe salientar que o primeiro PDA-CVM foi lançado em 2016, por meio da Portaria
CVM/PTE/n° 180, de 15/12/2016, com pleno alinhamento à Política de Dados Abertos
do Poder Executivo Federal, instituída pelo Decreto n" 8.777, de 11 de maio de 2016, que
visa, entre outros objetivos, aprimorar a cultura de transparência pública, franqueando ao
cidadão o acesso, de forma aberta, aos dados produzidos ou acumulados pela
Administração Pública1. Desde então, a Autarquia tem ampliado sua transparência ativa
e as bases de dados que estão disponíveis ao cidadão em seu portal de dados abertos
(https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/dados-abertos).
O presente plano também considera os princípios e diretrizes estabelecidos pela
Resolução nº 3, de 13 de outubro de 2017, do Comitê Gestor da lnfraestrutura Nacional
de Dados Abertos (CGINDA)2 que aprovou normas sobre a elaboração e publicação de
Planos de Dados Abertos; a lnstrução Normativa STL nº 4, de 12 de abri1 de 2012, que
criou a Infraestrutura Nacional de Dados Abertos (INDA)3, a Política Nacional de
Governo Aberto (Decreto nº 10.160, de 09 de dezembro de 2019), além dos parâmetros
estabelecidos na arquitetura de interoperabilidade do governo eletrônico e os vocabulários
e ontologias de Governo Eletrônico.

Deve ser salientado que o PDA-CVM não se aplica apenas aos dados gerados pela Autarquia,
mas também àquelas informações recebidas de participantes do mercado de capitais,
encaminhadas de forma voluntária ou com atenção à legislação ou regulamentação aplicável.
Nesse sentido, cabe destacar que a própria lei que instituiu a CVM exige que o exercício das
atribuições da Autarquia deve perseguir algumas finalidades (art. 4°, Lei n° 6.385, de 7 de
dezembro de 1976), entre elas a de "asseguraro acesso do público a informações subre
os valores mobiliários negociados e as
3
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 4

companhias que os tenham emitido". Essa é uma questão sensível, pois muitos dados de
terceiros envolvem informações pessoais, sendo especialmente aplicáveis as regras da Lei
Geral de Proteção de Dados (LGPD), a Lei nº 13.709, de 14 de agosto de 2018.
Assim, ao longo de sua história, a Autarquia sempre exigiu que os participantes de mercado
encaminhassem informações periódicas e eventuais. Esse acervo documental, aliado àquele
que foi produzido pela própria CVM no exercício de suas atribuições, contém um registro
importante, e muitas vezes único, das atividades exercidas pela Comissão em quase 50 anos
de existência, o qual observa, cumpre salientar, as diretrizese regras da política nacional
de arquivos públicos e privados (Lei 11° 8.159, de 3 de janeiro de 2002). Evidentemente, nem
todas as informações são destinadas a guarda permanente, sendo algumas eliminadas
segundo a regulamentação aplicável em cada momento.

2. CENÁRIO INSTITUCIONAL
A elaboração desta nova edição do PDA-CVM considerou os valores, as prioridades e os
objetivos estabelecidos pelo Planejamento Estratégico da CVM ("Construindo a CVM
de 2027").4

O documento foi elaborado por meio de processo de construção coletiva que confirmou
e atualizou os valores da CVM, cabendo destacar os seguintes, por sua pertinência com
o tema desta publicação:


COOPERAÇÃO: Somos comprometidos com um ambiente de trabalho cordial, que
preza pela cooperação e constante diálogo entre as diferentes áreas e níveis
hierárquicos;



DIÁLOGO: Sempre buscamos interagir com o mercado, a sociedade, o governo e
os órgãos internacionais;



TRANSPARÊNCIA: Prezamos pela transparência e ampla divulgação das
informações, nos termos da legislação;



FOCO

EM

RESULTADO:

Atuamos

continuamente

na

promoção

do

desenvolvimento, integridade e eficiência do Mercado de Valores Mobiliários.

Outros documentos importantes, do ponto de vista do cenário institucional de elaboração
do PDA-CVM, são a Política de Governança de Tecnologia da Informação (PGTI), em
4
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 5

especial a governança de dados por ela estabelecida, e o Plano Diretor de Tecnologia

da Informação (PDTI) da Autarquia. Como instrumento de diagnóstico, planejamento e
gestão, o PDTI alinha os investimentos em TI ao planejamento estratégico da Autarquia,
orientando o processo de tomada de decisão. Entre as diretrizes que orientamo plano está
a prioridade a ser dada à adoção de padrões abertos no desenvolvimento detecnologia da
informação e comunicação. Cabe destacar que sua concepção e monitoramento são
conduzidos por um comitê específico, o Comitê de Gestão de Tecnologia da Informação
e Transformação Digital - CGTI, instituído pela Portaria CVM/PTC/N° 197, de 22 de
novembro de 20195.

Finalmente, em linha com a Política Nacional de Arquivos, a CVM editou cm 2021 a sua
Política de Gestão de Documentos, que busca assegurar o direito fundamental de acessoà
informação, promovendo a transparência da gestão, por meio da organização e preservação
do acervo de documentos e processos, independentemente do suporte e franqueando sua
consulta àqueles que dela necessitem.

3. OBJETIVOS
3.1. OBJETIVO GERAL
Promover a abertura de dados na CVM, zelando pelos princípios da publicidade,
transparência e eficiência, segundo as diretrizes a seguir mencionadas:



expansão do número de bases de dados abertas (quantidade de dados);



melhoria da qualidade dos dados disponibilizados, de forma a contribuir para
a tomada de decisão pelos gestores públicos e incentivar o controle social
(qualidade dos dados); e



compromisso com a progressiva ampliação do compartilhamento de dados com
outros órgãos da administração pública federal, nos termos do Decreto n° 10.046,
de 9 de outubro de 20196.

3.2. OBJETIVOS ESPECÍFICOS
Os seguintes objetivos específicos deverão ser alcançados pela implementação do
presente PDA:
5
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 6



Identificar e priorizar a abertura de dados com grau de relevância para o cidadão;



Estimular o controle social;



Fornecer dados atualizados e os respectivos históricos, melhorando a
qualidade dos dados disponibilizados;



Apoiar a pesquisa e estudos técnicos e acadêmicos, contribuindo para a
produção de conhecimento no âmbito do mercado de valores mobiliários;



Incrementar os processos de transparência ativa; e



Fomentar propostas de inovação e de desenvolvimento tecnológico e sustentável.

4. CONSTRUÇÃO E EXECUÇÃO DO PLANO DE DADOS ABERTOS
Esta nova edição do PDA-CVM considerou os valores, as prioridades e os objetivos
estabelecidos pelo Planejamento Estratégico da CVM, conforme discriminado em
maiores detalhes no item 2.
Assim, a Assessoria de Análise Econômica, Gestão de Riscos e Integridade (ASA), a
Superintendência de Tecnologia da Informação (STI) e a Superintendência de Proteção
e Orientação aos lnvestidores (SOI) atuaram de forma colaborativa para mapear todas as
bases de dados existentes na CVM, de modo a avaliar quais deveriam ser abertas, levando
em consideração as demandas do público, as bases abertas já disponíveis e as exigências
de transparência ativa. A Superintendência de Tecnologia da Informação (STI) avaliou a
viabilidade tecnológica da abertura, enquanto cada componente organizacional
responsável pelo preparo e atualização dos dados avaliou a viabilidade operacional.
Demandas do cidadão, pesquisas1, e consultas junto ao público, conforme descrito na
seção abaixo, foram também consideradas como insumos para a elaboração do presente
PDA.
Assim, após criteriosa avaliação da ASA, SOI, STI e de cada componente gerador dos
dados, sob a coordenação da Superintendência Geral (SGE), a CVM elaborou o atual
Plano de Dados Abertos, a ser revisado periodicamente.

5. DADOS SELECIONADOS PARA A ABERTURA
1

Percepção dos usuários sobre a plataforma e os dados quantitativos disponibilizados pela CVM

6
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 7

O processo de seleção dos dados a serem abertos, contou com insumos da pesquisa citada
anteriormente, realizada em 2020, avaliação com as áreas técnicas responsáveis pelos dados,
a fim de entender os temas mais demandados, pedidos de informações recebidos do público,
temas tratados em reuniões, etc, por meio de reuniões com cada uma das áreas interessadas.
Adicionalmente, com o intuito de aprimorar o processo de abertura de dados da CVM e após
interações com o Núcleo de Dados Abertos da CGU, realizamos uma nova consulta pública
junto ao público, para que os usuários de nossas bases de dados pudessem opinar sobre suas
atuais preferências.
Sobre o conteúdo da pesquisa, além de apresentarmos o inventário para que o cidadão pudesse
assinalar as bases de maior interesse, foram incluídas perguntas para mapear a frequência e
perfil de acesso às informações disponibilizadas, eventuais sugestões, críticas e comentários.
O questionário disponibilizado ao público, no período de 07 a 24 de Março de 2024
(https://www.gov.br/cvm/pt-br/assuntos/noticias/2024/cvm-lanca-questionario-para-aprimorar-acesso-asinformacoes-disponibilizadas-pelo-regulador), teve a contribuição de 87 respondentes, conforme

tabela resumo abaixo.
ATUAÇÃO
Setor Privado
Investidor Pessoa Física
Setor Público
Investidor Institucional
Academia
TOTAL

QUANTIDADE
41
20
17
6
3
87

%
47
23
20
7
3
100

Em relação a frequência de acesso, observou-se que aproximadamente 47% acessam sempre
ou muitas vezes o Portal de Dados Abertos e, aproximadamente 53% responderam acessar
raramente, nunca ter acessado e até mesmo não conhecer o Portal. O resultado pode ser
verificado na Tabela abaixo:

FREQUÊNCIA DE ACESSO
Sempre
Muitas vezes
Às vezes
Raramente

QUANTIDADE
18
23
14
13

%
21
26
16
15
7

Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 8

Nunca
Não conheço o Portal de Dados Abertos
TOTAL

6
13
87

7
15
100

Foi solicitado que os respondentes indicassem até 4 bases/temas, conforme suas preferências
de abertura. O resultado, já ordenado, está organizado na tabela a seguir:

BASES

Quantidade

14. Portal Institucional – informações sobre regramentos editados,
decisões do Colegiado, comunicados e notícias, acordos de
cooperação, etc
6. Informações sobre Operações/Negociações de Ativos

40

8.

Consultas, Reclamações e Denúncias de Investidores

4. Processos e Documentos Administrativos - Processos
Sancionadores
3. Atos Declaratórios emitidos pela CVM
5. Processos e Documentos Administrativos - Companhias:
Recompra de Ações
1. Documentos Periódicos e Eventuais de Regulados Securitizadoras: Documentos: Informe Mensal de Outros Títulos de
Securitização
2. Documentos Periódicos e Eventuais de Regulados – Informe de
investidor não-residente.
7. Informações sobre Desvio e Performance de Auditores
Independentes
9. Informações sobre audiências de cidadãos junto aos setores da
CVM
10. Informações sobre Recursos Humanos da CVM (histórico
funcional, frequência, avaliações de desempenho etc.)
15. Outras
11. Demandas internas de Tecnologia da Informação
12. Informações patrimoniais de bens móveis e requisições
derivadas
13. Administração – Gastos administrativos diversos (telefonia,
reprografia, diárias e passagens, etc)

39
34
32
25
23
20
18
12
11
9
9
8
6
6

Os temas “Operações/Negociações de Ativos” e “Consultas, Reclamações e Denúncias de
Investidores” ainda não são passíveis de abertura no presente ciclo do PDA da CVM. Ambas
as informações possuem dados sigilosos ou com restrição de acesso, e ainda carecem de
aperfeiçoamentos em sua organização e discussões sobre o nível de agregação e
desidentificação das informações, no caso da abertura de informações relacionadas à
negociação de ativos.
As informações relativas ao Portal Institucional, por sua vez, constituem-se de textos não
estruturados, tais como normas, decisões do Colegiado, notícias e comunicados, muitos
desses em formato PDF ou Word. A natureza não estruturada desse conteúdo impõe
8
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 9

limitações para a sua abertura no presente ciclo. Não obstante, todas essas informações já
estão disponíveis publicamente na Web2 e o conteúdo relativo à atuação sancionadora (uma
das principais atividades da CVM, com forte apelo público e grande volume de consultas em
nossos sistemas) já está contemplado no conjunto de dados “Processos e Documentos
Administrativos - Processos Sancionadores”.
No que diz respeito às demais sugestões recebidas, foram algumas poucas contribuições, e
bastante heterogêneas, tais como incluir dados que, em alguns casos, já estão disponíveis no
Portal, como informações periódicas, e outras demandas que fogem do escopo, por referirem
a dados não estruturados ou mesmo não recepcionados pela Autarquia.
Além disso, houve comentários em torno da necessidade de melhoria sobre a forma de
consulta das informações no Portal Dados Abertos.
Por fim, considerando a viabilidade de abertura, restrições inerentes aos dados, e a relevância
dos insumos recebidos de todos os participantes envolvidos (internos e externos), bem como
os pontos acima destacados, foi decidido concentrar os esforços na abertura dos dados do 4º
ao 8º conjunto mais pontuados acima.

6. O PROCESSO DE CATALOGAÇÃO
A catalogação dos dados no Portal Brasileiro de Dados Abertos é de responsabilidade de
cada uma das Superintendências responsáveis pelos dados, sob a coordenação da
Superintendência de Tecnologia da lnformação da CVM (STI). Sempre que possíve1,
essa atividade é realizada de forma automatizada, observando-se as informações
prestadas pela Superintendência responsável, cabendo à STI o controle das estatísticas
de publicação e atualização das referidas bases de dados.

7. SUSTENTAÇÃO, MONITORAMENTO E CONTROLE
Os componentes organizacionais da CVM que geraram as informações ou que têm
responsabilidade pela sua requisição aos participantes de mercado são os responsáveis
por verificar a acurácia e qualidade das informações nos metadados respectivos. A
curadoria da publicação dos dados é de responsabilidade da ASA, SOI e STI, sob a
2

https://www.gov.br/cvm/
https://conteudo.cvm.gov.br/

9
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 10

coordenação do SGE, cabendo-lhes propor melhorias nos processos de abertura de dados
e nas bases abertas, tanto do ponto de vista quantitativo quanto qualitativo.
Sem prejuízo dessa atuação conjunta pela melhoria da qualidade e expansão das bases de
dados abertas pela CVM, caberá a cada um dos componentes organizacionais abaixo
mencionados as seguintes responsabilidades específicas:



ASA: identificar e propor melhoria na qualidade dos dados abertos;



STI: monitorar a disponibilidade dos arquivos catalogados e verificar se os padrões da
INDA e INDE ( metadados atualizados contendo a descrição, contatos dos responsáveis
pelas informações e dos outros metadados associados a cada conjunto de dados) estão
sendo observados.

O PDA-CVM é acompanhado e monitorado pelo SGE, com o apoio da ASA, SOI e STI.
A SOI é responsável pela disponibilização do PDA ao cidadão, cabendo-lhe também:



receber, processar e responder a sugestões, consultas e reclamações do público
externo no que se refere ao PDA-CVM e os dados abertos, por meio do SAC (Serviço
de Atendimento ao Cidadão), do e-SIC (Serviço de Informação ao Cidadão) ou de
outro canal disponível ao cidadão;



atualizar a Carta de Serviços ao Usuário para fazê-la refletir o PDA-CVM;



orientar os serviços de atendimento ao público no sentido de esclarecerem dúvidas e
prestarem orientações quanto ao acesso aos dados, bem como sobre os procedimentos
para requerer a abertura de uma base de dados; e



fazer levantamentos junto aos investidores e ao cidadão quanto a interesse na abertura
de dados, construindo mecanismos de participação social para aprimoramento do
PDA•CVM.

10
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 11

8. PLANO DE AÇÃO
Esta seção detalha as atividades e responsabilidades relacionadas ao processo de publicação de dados, incluindo prazos e requisitos.
8.1. CRONOGRAMA DE ELABORACÃO E SUSTENTAÇÃO DO PDA
Id.

Ação

Atividades

Objetivo

Responsáveis

Prazo

1

Planejar a abertura das bases de
dados selecionadas na lista
priorizada.

Estabelecer cronograma de ações
necessárias para a publicação em formato
aberto das bases selecionadas, conf'orme a
lista priorizada.

Definir, com as unidades, as ações necessárias para a abertura
das bases de dados selecionadas na lista priorizada e estabelecer
os respectivos cronogramas.

ASA, STI

SET/23-MAI/24

2

Elaboração do PDA 2024-2026.

Revisão do PDA.

Promover a atualização do PDA.

SGE, ASA, SOI, STI

MAI/24

3

Divulgar a lista de bases de dados.

Elaborar plano de comunicação para a
divulgação da abertura das bases de dados
selecionadas na lista priorizada do PDA.

Definir ações de comunicação necessárias para dar ampla
publicidade à divulgação da abertura das bases de dados
selecionadas na lista priorizada do PDA.

ASC

JUN/24

4

Realizar a abertura das bases
de dados selecionadas.

Executar as ações necessárias para
a publicação em formato aberto das bases
selecionadas na lista priorizada do PDA,
conforme cronograma estabelecido.

Disponibilizar para a sociedade, em formato aberto no portal de
dados da CVM, as bases selecionadas na lista priorizada do
PDA.

STI

JUN/24-MAI/26

5

Planejar nova abertura de
bases de dados.

Revisão do PDA.

Promover a atualização do PDA.

ASA, STI

SET/25-MAI/26

6

Elaboração do PDA 2026-2028.

Revisão do PDA.

Promover a atualização do PDA.

SGE, ASA, SOI, STI

MAI/26

7

Divulgar nova lista de bases de
dados

Revisão do PDA.

Promover a atualização do PDA.

ASC

JUN/26

Este plano não inclui as ações e respectivas atividades já iniciadas, em especial a disponibilização das bases de dados definidas nas
versões anteriores do PDA, sob a responsabilidade da ASA, STI e SOI.

11
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 12

8.2. CRONOGRAMA DE ABERTURA DE BASES – 2024 e 2025

Nome da base de
dados
Documentos Periódicos e
Eventuais de Regulados

Unidade e contato do
responsável pela base/
conjunto de dados

Frequência de
atualização

Meta/ Prazo
para abertura

Conjunto de dados

Descrição da base/conjunto de dados

Securitizadoras: Documentos:
Informe Mensal de Outros Títulos
de Securitização

Documentos não estruturados entregues pelas
companhias securitizadoras

SSE - Superintendência de
Securitização e Agronegócio
(sse@cvm.gov.br)

Semanal

30/06/2024

Diária

31/12/2024

Atos Declaratórios

Atos Declaratórios

Registros da existência ou não de autorização da
CVM para que determinada pessoa exerça
atividades no mercado de valores mobiliários

SMI - Superintendência de Relações
com o Mercado e Intermediários
(smi@cvm.gov.br)
SNC - Superintendência de Normas
Contábeis e de Auditoria
(snc@cvm.gov.br)
SIN - Superintendência de Supervisão
de Investidores Institucionais
(sin@cvm.gov.br)

Processos e Documentos
Administrativos

Processos Sancionadores

Informações públicas sobre processos
administrativos sancionadores

SPS - Superintendência de Processos
Sancionadores (sps@cvm.gov.br)

Semanal

30/06/2025

Processos e Documentos
Administrativos

Companhias: Recompra de Ações

Histórico de recompra de ações das companhias

SEP - Superintendência de Relações
com Empresas (sep@cvm.gov.br)

Semanal

31/12/2025

12
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 13

8.3. CRONOGRAMA DE PROMOÇÃO, FOMENTO, USO E REUSO DAS BASES

Produto

Atividades

Unidade e contato do
Responsavel

1.
Publicação
de materiais
informando sabre a publicação de
bases e o seu conteúdo

Publicar matérias, no site da CVM e chamadas nas redes
sociais institucionais, em meses de publicação de bases.

ASC

2. Consolidação de conhecimento.

Publicar matéria anual, no site da CVM e chamadas nas
redes sociais institucionais, consolidando a atividade
anual de abertura de dados.

ASC/ASA/STI

1° trimestre 2025.

3. Consolidação de conhecimento.

Publicar matéria anual, no site da CVM com chamadas
nas redes sociais institucionais, consolidando a atividade
anual de abertura de
Dados.

ASC/ASA/STI

1° trimestre 2026.

Data/periodo

Mês corrente OU subsequente à
abertura de nova base.

13
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 14

ANEXOS
A - INVENTÁRIO DE BASES DE DADOS DA CVM
Nome da base
de dados

Descrição da base

Unidade(s)
responsável(is)
pela base

Disponível em
dados.gov.br?

Conjuntos de dados abertos

Periodici
dade de
atualizaç
ão

Cadastro de
Regulados

Informações
cadastrais de
participantes de
mercado

SIN, SEP, SMI,
SRE, SNC, SSE

Parcialmente



Diária
















Administradores de Carteira:
Informação Cadastral
Administradores de FII: Informação
Cadastral
Agentes Autônomos: Informação
Cadastral
Agentes Fiduciários: Informação
Cadastral
Auditores: Informação Cadastral
Cias Abertas: Informação Cadastral
Cias Estrangeiras: Informação
Cadastral
Cias Incentivadas: Informação
Cadastral
Consultores de Valores Mobiliários:
Informação Cadastral
Emissores
Emissores de CEPAC: Informação
Cadastral
Fundos de Investimento: Informação
Cadastral
Participantes Intermediários:
Informação Cadastral
Plataformas de Crowdfunding:
Informação Cadastral
Representantes de Investidores Não
Residentes: Informação Cadastral

Política
pública
relacionada,
quando
aplicável

Possui
conteúdo
sigiloso ou
alguma outra
restrição de
acesso?
Sim

14
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 15

Documentos
Periódicos e
Eventuais de
Regulados

Informes e
documentos
entregues à CVM por
participantes de
mercado

SIN, SEP, SMI,
SNC, SSE, SOI

Parcialmente





















Cias Abertas: Documentos:
Formulário Cadastral (FCA)
Cias Abertas: Documentos:
Formulário de Demonstrações
Financeiras Padronizadas (DFP)
Cias Abertas: Documentos:
Formulário de Informações
Trimestrais (ITR)
Cias Abertas: Documentos:
Formulário de Referência (FRE)
Cias Abertas: Documentos: Informe
do Código de Governança (ICBGC)
Cias Abertas: Documentos:
Periódicos e Eventuais (IPE)
Cias Abertas: Documentos: Valores
Mobiliários Negociados e Detidos
FIDC: Documentos: Informe Mensal
FII: Documentos: Demonstrações
Financeiras
FII: Documentos: Informe Anual
Estruturado
FII: Documentos: Informe Mensal
Estruturado
FII: Documentos: Informe Trimestral
Estruturado
FIP: Documentos: Informe
Trimestral
Fundos Estruturados: Documentos:
Balancete
Fundos Estruturados: Documentos:
Balanço Semestral
Fundos Estruturados: Medidas
Fundos de Investimento:
Documentos: Balancete
Fundos de Investimento:
Documentos: Composição e
Diversificação das Aplicações
Fundos de Investimento:
Documentos: Eventuais, DFs e
Demonstrativos Trimestrais

Semanal

Sim

15
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 16



SRE

Parcialmente




GEARC/SAD,
GJU-3/PFE
SMI, SNC, SIN

Parcialmente



Arrecadação: Receita Pública

Atos
Declaratórios

Informações sobre
ofertas de valores
mobiliários,
emissores e
ofertantes
Informações sobre
multas, taxas, débitos
Registros da
existência ou não de
autorização da CVM
para que
determinada pessoa
exerça atividades no
mercado de valores
mobiliários

Fundos de Investimento:
Documentos: Extrato das
Informações
Fundos de Investimento:
Documentos: Formulário de
Informações Complementares
Fundos de Investimento:
Documentos: Informe Diário
Fundos de Investimento:
Documentos: Lâmina de Informações
Essenciais
Fundos de Investimento:
Documentos: Perfil Mensal
Securitizadoras: Documentos:
Demonstrações Financeiras de CRA
Securitizadoras: Documentos:
Demonstrações Financeiras de CRI
Securitizadoras: Documentos:
Informe Mensal de CRA
Securitizadoras: Documentos:
Informe Mensal de CRI
Ofertas Públicas
Ofertas Públicas de Distribuição

Não

Não

Processos e
Documentos
Administrativ
os

Informações sobre
processos
administrativos,
andamentos,

DINF/SAD,
SPS, SSR, SEP

Não

Sim









Ofertas
Públicas de
Distribuição
Arrecadação

Diária

Sim

Quinzena
l

Sim

16
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 17

Operações/Ne
gociações

Desvios e
Performance
de Auditores
Independentes
Consultas,
Reclamações e
Denúncias de
Investidores

Audiência a
Particulares
Recursos
Humanos

Demandas de

documentos,
processos
sancionadores,
acusados,
investigados,
decisões, penalidades
Informações sobre
investidores,
emissores, fundos de
investimento,
intermediários, fatos
relevantes, ordens,
negócios, posições,
cotações de ativos
Informações sobre
desvios e
performances de
auditores
independentes
Informações do
Serviço de
Atendimento ao
Cidadão (SAC) da
CVM: consultas,
reclamações,
sugestões, denúncias
Informações sobre
audiências de
cidadãos junto aos
setores da CVM
Informações sobre
servidores, histórico
funcional,
movimentações,
afastamentos,
frequência, planos de
metas, avaliações de
desempenho,
pontuações por
desempenho, ofertas
de benefícios
Informações sobre

SMI

Não

Sim

SNC

Não

Sim

GOI/SOI

Não

Sim

DINF/SAD

Não

Sim

SGP

Não

Sim

STI

Não

Sim

17
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 18

TI

Patrimônio
Administração

Portal
Institucional

demandas de TI,
ordens de serviço,
contratos,
prestadores de
serviço, serviços,
incidentes,
problemas, dúvidas
Informações sobre
tombos, bens móveis,
ordens de serviço
Informações sobre
gastos com serviços
de reprografia,
telefonia, garagem,
diárias e passagens
Legislação, decisão
do colegiado,
contratos, licitações,
institucional,
notícias, informações
sobre participantes
de mercado

GEMAP/SAD

Não

Não

SAD

Não

Não

ASC

Não

Não

18
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 19

B - DIRETRIZES GERAIS
Abrangem os fundamentos e critérios para seleção dos dados a serem abertos.
Os seguintes critérios são considerados pela CVM, desde o primeiro PDA:



Origem dos dados: A CVM, no exercício de suas atribuições, recebe e
processa dados de diferentes fontes: órgãos e entidades públicas,
provedores de serviços de informações e participantes de mercado (estes
ao cumprir obrigações estabelecidas pela legislação e regulamentação
de mercado). Esse conjunto de informações éheterogêneo e apenas a
análise caso a caso pode indicar o melhor procedimento para abertura.
Todavia, como procedimento geral, entende-se que os dados fornecidos
por participantes supervisionados pela CVM, salvo exceções previstas
estabelecidas na legislação aplicável, são os mais vocacionados para
disponibilização em formato abcrto, com respectiva publicação no
Portal Brasileiro de Dados Abertos (https://dados.gov.br/home).



Dcmanda pcla informação: A disponibilização pública de dados está
em consonância com a atribuicão legal da Autarquia de proteger
investidores que operam no mercado de valores mobiliários. Um dos
fatores cruciais para esse objetivo é o provimento de informações para
que os invcstidorcs possam tomar decisões informadas e acompanhar os

seus investimentos, reduzindo dessa forma os problemas decorrentesde
assimetria de informacões, que incluem questões relacionadas à seleção
adversa e ao risco moral.



Informações públicas: Parte substancial das informações encaminhadas à
CVM por participantes de mercado já está disponível na página da
Autarquia na Internet, embora, em alguns casos, sem dados históricos.
Como diretriz geral, devem ser abertos e disponibilizados todos os dados
de domínio público.



Formato na recepção: A CVM requer dos administradores das
companhias abertas e dos fundos de investimento urn conjunto bastante
abrangente de informações e dados. Nesse sentido, diversos formatos são
utilizados no envio dos documentos, dependendo do conteúdo das
informações. Algumas informacões, por exemplo, são encaminhadas de
forma eletrônica, em formato PDF, outras, por sua
19
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 20

vez, são enviadas em formato texto, com campos de formulários
específicos, havendo ainda aquelas fornecidas de forma estruturada,
de fácil agregação ou consolidação. Por fim, há ainda documentosque
combinam informações estruturadas com outras em forma de textolivre.
Como critério, será priorizada a abertura de dados estruturados, pela
facilidade futura de manuseio direto pelos usuários, sem prejuízo da
possibilidade de envio de informacões na forma de texto livre.



Questões de ordem tecnológica e de qualidade: Há a necessidade de
avaliação detalhada sobre a viabilidade de publicação no Portal de Dados
Abertos de cada série histórica de dados, tanto em termos tecnológicos
quanto em termos de qualidade dessas informações. Nesse sentido, há
priorização para dados que decorram de exigências normativas em vigor há
pelo mcnos 2 anos. Esse critério visa assegurar a qualidade da informação,
pois há uma natural curva de aprendizagem por parte das entidadcs
rcguladas pcla CVM toda vcz que nova obrigação informacional é
instituída.

C - ESTRATÉGIAS PARA ABERTURA
Sob a coordenação do Superintendente Geral, a Assessoria de Análise Econômica, Gestão
de Riscos e Integridade (ASA), a Superintendência de Proteção e Orientação aos
Investidores (SOI) e a Superintendência de Tecnologia da Informação (STI) deverão, a
cada dois anos, reavaliar o conjunto de dados que poderá ser aberto. A decisão final
pela abertura levará em consideração os critérios de priorização definidos pela ASAe
pela SOI, neste caso considerando as demandas do público e as exigências de transparência
ativa. Avaliada a viabilidade tecnológica da abertura, pela STl, e operacional, junto ao
componente organizacional responsável pelo preparo e atualização dos dados, será
elaborada proposta de abertura. O PDA-CVM também será revisado periodicamente.

20
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 21

REFERÊNCIAS
1) Lei Complementar n° 101, de 4 de maio de 2000, determinando ao Poder Público a

adoção de instrumentos de transparência na gestão fiscal em meios eletrônicos de
acesso público às informações orçamentárias e prestações de contas;
2) Infraestrutura Nacional de Dados Abertos - INDA:



Instrução Normativa n° 4, de 13 de abril de 2012, que cria a INDA e estabelece
os seguintes conceitos: dado, informação, dado público, formato aberto, licença
aberta, dados abertos e metadado;



O Plano de Ação da INDA, que institui a necessidade de os órgãos de
instituírem seus respectivos Planos de Abertura de Dados com vistas a uma
Política Nacional de Dados Abertos e institui os elementos mínimos do
documento, bem como orienta que a abertura de dados deve observar a
relevância para o cidadão;

3) Política Nacional de Governo Aberto;
4) Lei nº 12.527, de 18 de Novembro de 2011 (Lei de Acesso à Informação - LAI);
5) Padrões de Interoperabilidade de Governo Eletrônico, chamados e-PING;
6) Vocabulários e Ontologias do Governo Eletrônico - e-VoG;
7) Modelo de Acessibilidade de Governo Eletrônico - e-MAG;
8) Planejamento Estratégico 2023-2027 e o PDTI da CVM.

21
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 22

GLOSSÁRIO
Dado - sequência de símbolos ou valores, representados em qualquer meio, produzidos
como resultado de um processo natural ou artificial;
Dado acessível ao público - qualquer dado gerado ou acumulado pelo Governo que não
esteja sob sigilo ou sob restrição de acesso nos termos da Lei n° 12.527, de 18 de
novembro de 2011;
Dados abertos - dados acessíveis ao público, representados em meio digital, estruturados
em formato aberto, processáveis por máquina, referenciados na internet, disponibilizados,
sob licença aberta ou sob domínio público que permita sua livre utilização, consumo
ou cruzamento, limitando-se a creditar a autoria ou a fonte;
Dados Abertos Governamentais - metodologia para a publicação de dados do governo
em formatos reutilizáveis, visando o aumento da transparência e maior participação
política por parte do cidadão, além de gerar diversas aplicações desenvolvidas
colaborativamente pela sociedade;

Formato aberto - formato de arquivo não proprietário, cuja especificação esteja
documentada publicamente e seja de livre conhecimento e implementação, livre de patentes
ou qualquer outra restrição legal quanto a sua utilização;
Governança Digital - utilização, pelo selor público, de tecnologias da informação e
comunicação com o objetivo de melhorar a informação e a prestação de serviços,
incentivando a participação dos cidadãos no processo de tomada de decisão e tornando
o governo mais responsável, transparente e eficaz; e
Plano de Dados Abertos - documento orientador para as ações, com prazos definidos,
de implementação e promoção de abertura de dados de cada órgão ou entidade da
administração pública federal, obedecidos os padrões mínimos de qualidade, de forma
a facilitar o entendimento e a reutilização das informações.

22
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 23

NOTAS
¹O Plano de Ação para 2017 (anexo I), contido na primeira versão desde documento
foi plenamente executado e culminou na abertura de 100% dos dados selecionados pela
CVM no Portal de Dados Abertos do Governo Federal.

²Resolução n º 3, de 13 de outubro de 2017

³INSTRUÇÃO NORMATIVA No - 4, DE 12 ABRIL DE 2012

4

Planejamento Estratégico da CVM

5

PORTARIA CVM/PTE/Nº 197, DE 22 DE NOVEMBRO DE 2019

6

DECRETO Nº 10.046, DE 9 DE OUTUBRO DE 2019

7

A lnfraestrutura Nacional de Dados Abertos (INDA) é um conjunto de padrões,
tecnologias, procedimentos e mecanismos de controle necessários para atender às
condições de disseminação c compartilhamento de dados e informações públicas no
modelo de Dados Abertos. A INDA é a política do governo brasileiro para dados abertos.

8

Plano de Ação da INDA

9

DECRETO Nº 10.160, DE 9 DE DEZEMBRO DE 2019

10

Padrões de Interoperabilidade de Governo Eletrônico - ePING

11

Vocabulário Controlado do Governo Eletrônico - VCGE

12

https://emag.governoeletronico.gov.br/

23
Anexo A à Portaria PTE 51/2024 (2043923)

SEI 19957.015409/2023-54 / pg. 24
