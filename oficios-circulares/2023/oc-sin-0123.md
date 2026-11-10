---
titulo: "Ofício Circular CVM/SIN 01/23"
orgao: "Comissão de Valores Mobiliários"
tipo: "Ofício-Circular CVM"
numero: "01/23"
data: 2023-04-12
ementa: "Descontinuação do login nativo do sistema CVMWeb"
revogada: false
versao_texto: "publicação no portal da CVM"
fonte: "https://conteudo.cvm.gov.br/legislacao/oficios-circulares/sin/oc-sin-0123.html"
arquivo: "https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/oficios-circulares/sin/anexos/Documentacao_Tecnica_Plataforma_Supevisao_v11.pdf"
sha256_arquivo: a0cc08b5c90a05b0a0f10eea5742547320a60d029f01e437f7370d86698f112d
baixado_em: 2026-11-10
---
# Ofício Circular CVM/SIN 01/23

Comissão de Valores Mobiliários
API de recepção e processamento de Informes
Documentação Técnica – v1.1
1) Geração de Chaves de Acesso
Para se autenticar na API de recepção e processamento de informes, será
necessário o uso de chave de acesso gerada no CVMWeb, em área
identificada.
1) Após acessar o CVMWeb e se identificar (login), acessar no menu à
esquerda a opção ‘Chaves de Acesso’:

2) Dentro da funcionalidade, é possível gerar uma nova chave de acesso,
que ficará vinculada ao seu usuário/CPF, bem como visualizar as
chaves geradas:
2.1) Geração de chave de acesso:

2.2) Visualização das chaves de acesso, bem como opção de
revogação:

Com a chave de acesso gerada, será possível se autenticar na API e receber
um access token, utilizado para enviar informes.

2) Autenticação
Mediante parâmetros de autenticação, retorna token de acesso para envio de
informes ou acesso negado.


URL
PRODUÇÃO:
https://web.cvm.gov.br/services/auth/get/access/token
AMBIENTE DE TESTES/”SANDBOX”: (instruções abaixo)
https://web.cvm.gov.br/services/sandbox/auth/get/access/token

Method:
POST


Headers necessários no Request
Com a chave de acesso (secret) gerada conforme item anterior –
Geração de chaves de acesso, o “header” Authorization deve ir com o
seguinte valor (codificado em Base64):
CPF_usuário:chave_de_acesso
PARA TESTES, UTILIZE 1234 COMO CHAVE DE ACESSO PARA
QUALQUER CPF.

Ex: CPF 11111111111 e chave de acesso XXXXXX
No header, deve constar o valor 11111111111:XXXXXX codificado em
Base64, que equivale à String MTExMTExMTExMTE6WFhYWFhY.
O header do exemplo acima seria:
Nome
Authorization


Valor
Basic
MTExMTExMTExMTE6WFhYWFhY

Corpo da requisição (Request body)
Corpo vazio.



Resposta esperada (sucesso):
Situação
Autenticação
efetuada
com
sucesso

Código de
retorno HTTP
200 (OK)

Corpo da resposta
{
"access_token": "xxxx",
"token_type": "bearer",
"expires_in": 3600
}

Após o login bem sucedido, o retorno volta com três dados importantes:




O token de acesso (access_token)
O tipo do token (por padrão, bearer)
O tempo de vida do token, em segundos
o No exemplo acima, uma hora (padrão).

Com esses dados, sua aplicação já poderá enviar informes para o web
service durante o tempo de vida do token. Após sua expiração, um novo
token deverá ser gerado.


Respostas com erro:

Situação

Código de
Corpo da resposta
retorno HTTP
Autenticação 401 (Unauthorized) {
inválida
"error": "invalid_client",
"error_description": "Credenciais
invalidas"
}
Erro interno
500 (Internal
{“error_description”:“descrição do
Server Error)
erro”}

2) Processamento de informes
As instruções abaixo se referem ao uso da API para o envio e processamento
dos informes. Inicialmente, listamos as URLs por tipo de informe e na seção
posterior, os detalhes técnicos que são comuns a todos.

2.1) Processar Informes diários
Padrão XML:
https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/PadroesXML/PadraoXMLInfoDiar
ioNetV3.asp

URL
PRODUÇÃO:
https://web.cvm.gov.br/services/informes/api/informe/diario
AMBIENTE DE TESTES/”SANDBOX”:
https://web.cvm.gov.br/services/sandbox/informes/api/informe/diario

2.2) Processar Lâmina de Fundos
Padrão XML:
https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/PadroesXML/PadraoXMLLamina
V2.asp

URL
PRODUÇÃO:
https://web.cvm.gov.br/services/informes/api/informe/lamina
AMBIENTE DE TESTES/”SANDBOX”:
https://web.cvm.gov.br/services/sandbox/informes/api/informe/lamina

2.3) Processar Informe de Fundo 157
Padrão XML:
https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/PadroesXML/PadraoXMLInf157.a
sp

URL
PRODUÇÃO:
https://web.cvm.gov.br/services/informes/api/informe/fundo157
AMBIENTE DE TESTES/”SANDBOX”:
https://web.cvm.gov.br/services/sandbox/informes/api/informe/fundo157

2.4) Processar Informe de Prestadores de
Serviço
Padrão XML:
https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/PadroesXML/PadraoXMLPrest.as
p

URL
PRODUÇÃO:
https://web.cvm.gov.br/services/informes/api/informe/prestservicos
AMBIENTE DE TESTES/”SANDBOX”:
https://web.cvm.gov.br/services/sandbox/informes/api/informe/prestservic
os

2.5) Processar Informe Mensal de
Investidores Não Residentes
Padrão XML:
https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/PadroesXML/PadraoXMLInfoMen
salINR.asp

URL
PRODUÇÃO:
https://web.cvm.gov.br/services/informes/api/informe/mensalinr
AMBIENTE DE TESTES/”SANDBOX”:
https://web.cvm.gov.br/services/sandbox/informes/api/informe/mensalinr

2.7) Orientações gerais para envio dos
Informes
Para enviar qualquer um dos informes acima, valem as instruções
abaixo, variando apenas a URL e o XML enviado.


Method:
POST



Headers necessários no Request
Nome
Content-Type

Authorization

Valor
application/xml; charset=UTF-8
ou
text/xml; charset=UTF-8
[Token_Type] [Access_Token]

O header Content-Type pode receber qualquer um dos valores
especificados. Atente-se para o ‘encoding’ UTF-8, que é o esperado no
corpo da requisição.
O header Authorization receberá dois valores, separados por um
espaço em branco, como colocado acima. O primeiro deles é o tipo do
token (‘token type’), que é retornado pelo método de autenticação
(padrão: bearer) e o segundo o próprio token de acesso
(‘access_token’), também retornado pelo serviço.
Para o exemplo anterior, o header ficaria:
Authorization: bearer xxxx


Corpo da requisição (Request body)
No corpo da requisição deve ser enviado o conteúdo XML que já é
enviado à CVM atualmente e cujo padrão pode ser encontrado em
http://sistemas.cvm.gov.br -> Sistema CVMWeb -> Envio de
Documentos -> Padrões de Arquivos - XML e Outros.
Apesar de não ser obrigatório, é recomendável enviar o XML sem
formatação, quebras de linha ou espaços antes ou após as tags. O
retorno do processamento devolve um hash de verificação
(“checksum”) que não leva em consideração nenhum desses
caracteres.



Resposta esperada (sucesso):

Situação

Informe
processado

Código de
retorno
HTTP
200 (OK)

Corpo da resposta
(exemplo; maiores detalhes abaixo)
{
"protocoloRecebimento": 1234567,
"statusGeralProcessamento": "P",
"checksum":
"ca46003634a7d2478c606759fd04ec32c7da9fe5887a8c54a348a
439f40aa60f",
"dataHoraProcessamento": "14/07/2020 16:30:49",
"totalInformesProcessados": 3,
"detalhes": {
"11.111.111/1111-11": {
"protocoloProcessamento": 10000000,
"statusProcessamento": "E",
"mensagensAssociadas": [
"O usuário (CPF: XXXX) não possui permissão para
enviar informe diário para este fundo",
“mensagem de erro 2”,
“mensagem de erro 3”
]
},
"22.222.222/2222-22": {
"protocoloProcessamento": 10000001,
"statusProcessamento": "S",

"mensagensAssociadas": []
}
"11.111.111/1111-11": {
"protocoloProcessamento": 10000000,
"statusProcessamento": "E",
"mensagensAssociadas": [
"Patrimônmio Líquido inválido"
]
}
}
}

A resposta esperada não quer dizer que o informe foi processado com
sucesso, isso é detalhado no corpo do JSON retornado, como detalhado a
seguir. Um código de retorno 200 implica que o processamento ocorreu
sem falhas.
Detalhes do JSON de retorno
Chave
protocoloRecebimento

statusGeralProcessamento

Definição
Número do protocolo de recebimento –indica
que a CVM recepcionou o informe com
sucesso. Não implica automaticamente no
processamento do mesmo.
Indica o status geral do processamento do
informe enviado, podendo ter os seguintes
valores:

Valor
S

P

E

N

Significado
Sucesso – Todos os
informes
recepcionados foram
processados com
sucesso.
Sucesso parcial.
Indica que nem
todos os informes
foram processados
com sucesso.
Erro geral. Todos os
informes enviados
tiveram erros de
validação.
Erro interno –
Ocorreu algum erro
nos servidores da
CVM durante o
processamento.
Nesse caso, a

checksum

orientação inicial é
reenviar o informe e
caso o erro persista,
acionar o Suporte a
Sistemas da CVM.
Esse campo é uma “hash” usando o algoritmo
SHA-256 do XML enviado no corpo da
requisição. Na geração do hash todos os
espaços entre tags, no início e final do arquivo
são removidos, bem como a quebras de linha.
Por exemplo, o XML abaixo (formatado e com
espaços entre tags):
<CAB>
<INF1>xxx</INF1> <INF2>qqq</INF2>
</CAB>
<CORPO>
<A>b</A>
<B>c</B>
</CORPO>
Irá ser convertido para a seguinte “String”, em
linha única:
<CAB><INF1>xxx</INF1><INF2>qqq</INF2>
</CAB><CORPO><A>b</A><B>c</B></COR
PO>

dataHoraProcessamento
totalInformesProcessados
detalhes

protocoloProcessamento
statusProcessamento

mensagensAssociadas

É dessa última string que o checksum SHA256 será gerado e retornado.
Data e hora exata em que o processamento
do informe foi efetuado.
Total de informes processados.
Mapa com os detalhes do processamento.
Cada chave no mapa é um CNPJ dos que
foram enviados no informe e o valor é um
objeto com três chaves, conforme detalhado
abaixo.
Número do protocolo de processamento para
o CNPJ em questão.
Status do processamento do informe
específico, podendo ter os valores:
Valor
Significado
S
Sucesso
E
Erro
Lista de strings com mensagens detalhando
os erros. Se o processamento tiver sido com
sucesso, este campo será uma lista vazia.



Respostas com erro:

Situação
Token de acesso
inválido ou expirado
Erro interno

Código de retorno
HTTP
401 (Unauthorized)
500 (Internal
Server Error)

Corpo da resposta
