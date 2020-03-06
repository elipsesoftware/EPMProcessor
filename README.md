# EPM Processor

O **EPM Processor** é o módulo do **Elipse Plant Manager** reponsável pela execução de códigos em linguagem **Python**, baseados em eventos simulados ou de tempo real. 

* Documentação

  * [Guia Rápido de Utilização](quickstart/README.md) - Guia para entender os procedimentos para se inserir um algoritmo e colocá-lo em produção.
  * [Guia do Usuário](guiadousuario/README.md) - Guia completo para explorar todos os aspectos da ferramenta.
  * [Série de Vídeos](https://youtu.be/A1BF0tg71l8) - Série de vídeos sobre o EPM Processor.

* Exemplos

  * [Consulta com Agregação OPC UA](exemplos/aggregation_query.py) - Consulta de médias, interpolações, mínimas, máximas, etc,  utilizando as agregações do padrão OPC UA.
  * [Consulta Raw (Dados brutos)](exemplos/raw_query.py) - Consulta de dados brutos, ou seja, como foram gravados. 
  * [Escritas no EPM Server](exemplos/write_methods.py) - Escritas de conjuntos de dados ou dados únicos no EPM Server.
  * [Contexto de execução](exemplos/scope_context.py) - Alterando o fluxo de execuçaõo do algoritmo de acordo com o contexto em que está sendo executado: Teste, simulação ou produção.
  * [Buscando Resources no EPM Webserver](exemplos/get_resources.py) - Lendo arquivos do EPM webserver para utilizá-los como recurso do algoritmo. 
  * [Lógica Fuzzy](exemplos/fuzzy_thermal_comfort_kpi.py) - Modelo de lógica Fuzzy apresentado nos vídeos do EPM Processor.



  
