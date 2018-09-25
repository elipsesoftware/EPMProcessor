## Criando Algoritmos para o EPM Processor

[Retornar ao menu](menu.md)

**Sessões:**


[**Leitura de Dados**](EPMProcessorAlgoritmos.md#leitura-de-dados)

[**Escrita de Dados**](EPMProcessorAlgoritmos.md#escrita-de-dados)

[**Objetos do DataModel**](EPMProcessorAlgoritmos.md#objetos-do-datamodel)

[**Resources**](EPMProcessorAlgoritmos.md#acesso-aos-resources)

[**Contexto de Execução**](EPMProcessorAlgoritmos.md#contexto)

### Introdução

Quando se deseja implementar um algoritmo para ser utilizado no **EPM Processor**, seja em produção ou simulação, o mesmo deverá ser codificado dentro de uma função em linguagem Python que, neste caso, será designada por **Application Method**, ou simplesmente de **Method** <sup>1</sup> (método em português).
Para que uma função seja apresentada como um método do **EPM Processor** nas configurações das **Applications**, é necessário que a mesma seja identificada como tal, isso é feito através do uso de um *decorator* <sup>2</sup>, a ser visto mais adiante.

Veja o fluxo de criação e utilização de um método para aplicações no **EPM Processor**:

![fluxo algoritmo](./images/algoritmos_fluxo.PNG)



Existem duas bibliotecas que sempre devem ser importadas no código, uma do próprio **EPM Processor** e outra para acessar informações e dados de um **EPM Server**:

`import epmprocessor as epr`

`import epmwebapi as epm`
 
Essas bibliotecas provém todas as funcionalidades que veremos a seguir:

**O decorator *@epr.applicationMethod()***

Esse *decorator* deverá ser utilizado em todas as funções Python que serão expostas como métodos para utilização nas **Applications**.


Por exemplo:
```python
import epmprocessor as epr
import epmwebapi as epm

@epr.applicationMethod('MyMethod')
def my_method(session, param1, param2):
    '''Documentation'''
    
    ...
```

No exemplo acima, foi utilizado o parâmetro *session*. Este parâmetro deverá sempre receber o tipo *session* na entrada de dados do método. 
Através dele são acessíveis informações relativas ao evento, contexto de execução, informações sobre a última execução, etc.

O exemplo abaixo mostra o uso das propriedades *timeEvent* e *range* do parâmetro *session* para trabalhar com o período de uma consulta, relativo ao momento em que o método foi executado.
```python
import epmprocessor as epr
import epmwebapi as epm
import datetime

@epr.applicationMethod('MyMethod')
def my_method(session, param1, param2):
    
    endtime = session.timeEvent
    initime = endtime - datetime.timedelta(session.range)
    
    queryPeriod = epm.QueryPeriod(initime,endtime)

    pass
```

Lista de propriedades do parâmetro **session**:

|Propriedade|Descrição|
|---|---|
|timeEvent|Data/hora do evento que gerou a execução do método. Pode ser informado manualmente em caso de teste, em tempo real no caso de uma **Production** ou simulado no caso de uma **Simulation**|
|range|Intervalo de tempo. Usualmente utilizado em conjunto com o parâmetro *timeEvent* para determinar as datas de início e fim das consultas aos dados de processo|
|processInterval|Intervalo de tempo de processamento usado em consultas com agregação|
|parametersMap|Lista de parâmetros globais de uma **Application**, criados através do botão **New Session Parameter**|
|userCache|Memória de execução que pode ser usada para transferir informações entre uma execução e outra|
|lastExecutedInfo|Informações sobre a última execução|
|connections|Variável que contém todas as **connections** utilizadas pelos parâmetros de um método que exigem conexões com um **EPM Server**|
|scopeContext|Contém informações sobre o contexto de execução, ou seja, se a avaliação do método está sendo feita a partir de um teste, uma execução em produção ou em uma simulação. Veja mais [aqui](EPMProcessorAlgoritmos.md#contexto-de-execução).|

 :large_blue_diamond: Ao construir os métodos deve-se ter em mente que o seu número de parâmetros é fixo e configurado através do **Workbench**.
Então os métodos que utilizam o *decorator* `@epr.applicationMethod()` não devem utilizar `*args` ou `**kwargs` na construção.

:bulb: É possível criar parâmetros adicionais para a *session* através do botão **New Session Parameter**. Esse botão existe na área **Test** do **Code Package** para fins de teste. Para efetivamente usar em **Solutions**, esses parâmetros adicionais deverão ser configurados nas respectivas **Applications**.

**Parâmetros do método**

Esses são os tipos de dados disponíveis para serem usados na entrada de parâmetro dos métodos: 

|Tipo|Descrição|
|---|---|
|int|Tipo inteiro do Python|
|intArray|Sequência de inteiros, por exemplo: [1, 3, 5, 6]|
|float|Tipo ponto flutuante do Python|
|floatArray|Sequência de pontos flutuantes, por exemplo: [1.0, 3.5, 5.0, 6.1]|
|string|Tipo cadeia de caracteres do Python|
|stringArray|Sequência de cadeia de caracteres, por exemplo: ['abc','def','123']|
|bool| Tipo booleano do Python|
|boolArray|Sequência de booleanos, por exemplo: [true, false, false]|
|dictionary|Tipo dicionario ordenado do Python|
|datetime|Tipo data-hora do Python (o *Workbench* ajuda a preencher este campo com a ferramenta de calendário)|
|datetimeArray|Array de datetimes (o *Workbench* ajuda a preencher este campo com a ferramenta de calendário)|
|session| Tipo exclusivo do EPM Processor - recebe *datetime*, *range* e *process*|
|epmconnection|Tipo exclusivo do EPM Processor - recebe uma das conexões configuradas em *EPM Connections* |
|dataobject|Tipo exclusivo do EPM Processor - recebe uma das conexões configuradas em *EPM Connections* e um nome de *dataobject*|
|dataobjectArray|Lista de *dataobjects*|
|epmobjectDict|Tipo exclusivo do *EPM Processor* - recebe um das conexões configuradas em *EPM Connections*, um filtro baseado no nome do objeto e um tipo (Os filtros são case sensitive). Vai montar um dicionário ordenado do Python|


A seguir é apresentado uma série de exemplos de uso:

### Leitura de Dados de **Data Objects**


#### historyReadRaw()
Utilizamos esse método do *dataobject* para fazer consultas aos dados brutos (como foram armazenados) de um objeto de dados de um EPM Server, passando apenas o período de tempo da consulta como argumento.
Para trabalhar com períodos de tempo utiliza-se a classe *QueryPeriod*.

O retorno desta função corresponde a um *array* do módulo *numpy* com o seguinte cabeçalho: *Value*, *Timestamp* e *Quality*.

Exemplo:

```python
import epmwebapi as epm
import datetime

@epr.applicationMethod('GetHistoryRaw')
def get_history_raw(session, epmdataobject):
    '''Get one hour raw historic data from epm dataobject'''

     endtime = session.timeEvent

     initime = endtime - datetime.timedelta(session.range)

     queryperiod = epm.QueryPeriod(initime, endtime)

    try:
        data = epmdataobject.historyReadRaw(queryperiod)
    except:
        raise Exception('Error reading raw data.')
```

:warning: É uma prática altamente recomendada colocar as consultas históricas sempre dentro de um bloco *try/except* do Python!


#### historyReadAggregate()

Esse método faz consultas agregadas aos dados de processo conforme o padrão OPC UA. É preciso passar como parâmetro o período da consulta, o tipo de agregação e o intervalo da agregação.
Nesse caso utiliza-se, além da classe *QueryPeriod*, a classe *AggregateDetails*.

O retorno desta função corresponde a um *array* do módulo *numpy* com o seguinte cabeçalho: *Value*, *Timestamp* e *Quality*.

Exemplo:

```python
import epmwebapi as epm
import datetime

@epr.applicationMethod('GetHistoryInterpolative')
def get_history_interpolative(session, epmdataobject):
    '''Get interpolative data from epm dataobject'''
    
    endtime = session.timeEvent
    initime = endtime - datetime.timedelta(session.range)

    try:
        queryperiod = epm.QueryPeriod(initime,endtime)
        processInterval = datetime.timedelta(seconds=session.processInterval)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails,queryperiod)
    except:
        raise Exception('Error reading processed data.')
            
```
:warning: É uma prática altamente recomendada colocar as consultas históricas sempre dentro de um bloco *try/except* do Python!

Veja os tipos de agregações disponíveis no [Apendice A - Agregações](Agregacoes.md).


### Escrita de Dados em uma **Basic Variable**

Existem dois métodos para escrita de dados em uma **Basic Variable** de um **EPM Server**, cada um servindo a uma situação.

* **write()** - Utiliza a "via de tempo real" do **EPM Server**. Deverá ser utilizado quando se deseja escrever um valor único em um único em uma **Basic Variable**.

Para o dataobject receber uma escrita através dessa função é necessário que:
   * Não exista vínculo da **Basic Variable** com um endereço do **Interface Server**;
   * Esteja habilitada a opção *"Enable Real Time"* da **Basic Variable**;
   * Esteja habilitada a opção *"Record"* da **Basic Variable**.
  
  
* **historyUpdate()** - Utiliza a "via de dados históricos" do EPM Server. Utilizado para escrever uma sequência de valores em uma **Basic Variable**. Como argumento deve-se passar a seguinte estrutura de dados do tipo *numpy array*:

```python
import numpy as np
array_format = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', '>i4')])

```
> * A coluna *Value* foi definida para o tipo *floating point* ('>f8') do Python, caso os dados sejam de outro tipo, é necessário adequar este parâmetro para o tipo correspondente.
> * A coluna *Timestamp* deverá sempre receber dados do tipo *datetime* do Python, e sempre colocado em ordem cronológica natural, ou seja, dos mais antigos aos mais novos.
> * A coluna *Quality* deverá corresponder a uma qualidade do padrão OPC UA, para valores com qualidade boa o valor correspondente é zero.


:warning: *Evitar a escrita de dados fora de ordem cronológica. Quando o EPM Server recebe um valor fora de sequência, precisa de processamento extra para inserí-lo no ponto correto.*  


#### basicvariable.write(data)

Exemplo:

```python
import datetime

@epr.applicationMethod('Write')
def write(session, epmdataobject):
    '''Write one value in epmdataobject'''

    date = datetime.datetime.now()
    value = 100
    quality = 0 #zero is Good in OPC UA

    try:
        epmdataobject.write(value, date, quality)
    except:
        raise Exception('Error writing data.')
```


#### basicvariable.historyUpdate(data)

Neste exemplo também é verificado o contexto de execução do método: Test, Simulation ou Production. 
Veja mais detalhes sobre na documentação da Biblioteca epmprocessor.


```python
import epmprocessor as epr
import epmwebapi as epm
import numpy as np
import pandas as pd


@epr.applicationMethod('HistoryUpdate')
def history_update(session, epmdataobject):
    '''Update epmdataobject with five itens'''

    #pandas generate a range of dates
    newdates = pd.date_range('1/1/2018', periods=5,freq='H' )

    #just a five itens list
    newvalues = [50,60,30,40,10]

    # epm ndarray data format.
    desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', '>i4')])
    datatemp = np.empty(len(newvalues), dtype=desc)

    #loop to populate the object before send to EPM
    i=0
    while i < len(newvalues):
        datatemp['Value'][i] = newvalues[i]
        datatemp['Timestamp'][i] = newdates[i]
        datatemp['Quality'][i] = 0
        i = i+1
    try:

        if session.scopeContext == epr.ScopeContext.Test:
            print('Resultado: {valor} - {timestamp}'.format(valor=str(datatemp['Value'][-1]),
                                                                timestamp=datatemp['Timestamp'][-1].isoformat()))
        else:  # Production ou Simulation
            epmdataobject.historyUpdate(datatemp)

    except:
        raise Exception('Error in historyUpdate')
```
 


### Acesso aos Resources
É possível acessar a estrutura de arquivos dos recursos do **EPM Webserver** através da API. São acessíveis
tanto recursos do próprio **EPM Processor**, como também do **EPM Portal**.
Para acessá-los é necessário ter um parâmetro do tipo *epmconnection*, e a partir do qual são acessados os recursos. 

Para acessar recursos do **EPM Processor** utilize:

`resource_manager = epmconnection.getProcessorResourcesManager()`

Para recursos do **EPM Portal** utilize:

`resource_manager = epmconnection.getPortalResourcesManager()`


**Exemplos:**

**Download de recurso:**

```python
@epr.applicationMethod('ResourceAccess')
def resource_access(session, epmconnection):
    '''Access resource from EPM Processor '''
    
    resource_manager = epmconnection.getProcessorResourcesManager()
    image_resource = resource_manager.getResource('folder/image.png')
    image = image_resource.download(epm.DownloadType.Binary)   
 
```

**Upload de imagem para uma pasta do EPM Portal:**

```python
@epr.applicationMethod('UploadImage')
def upload_image(session, epmconnection, pathname):
    '''Upload matplotlib .png chart to EPM Portal resources folder '''
    
    some_data = [1,2,3,4,5]
    import matploptlib.pyplot as plt
    import io
    import mimetypes
    
    plt.plot(some_data)    
    buffer = io.BytesIO()    
    plt.savefig(buffer, format='png') #salva figura em buffer
    buffer.seek(0)
    
    resource_manager = epmconnection.getPortalResourcesManager()
    folder = resource_manager.getResource(pathname)
    
    #faz upload do buffer com o tipo .png
    resource = imgFolder.upload('image.png', buffer, 'matplotlib plot',
                                mimetypes.types_map['.png'], overrideFile=True)  
```


**Deletando um resource:**

```python
@epr.applicationMethod('Delete')
def delete_image(session, epmconnection):
    '''Delete EPM Portal resource'''  
      
    resource_manager = epmconnection.getPortalResourcesManager()    
    resource_manager.getResource(u'folder/image.png').delete()
```


### Objetos do Elipse Data Model (aplicações do Elipse E3 e/ou Elipse Power)

O **Elipse DataModel** permite replicar a estrutura de dados dos sistemas SCADA da Elipse (Elipse E3 e Elipse Power).

Uma vez que essa estrutura exista no **EPM Server** é possível localizar e trabalhar com seus elementos no código.

Uma das formas de obter esses elementos é utilizando o tipo **epmobjectDic** como parâmetro de entrada. Dessa forma o filtro é realizado no **EPM Server** e o parâmetro irá conter um objeto do tipo dicionário ordenado do Python com o resultado do filtro.

![epmobjectdict](images/algoritmos_epmobjectDict.PNG)

A tabela abaixo descreve os campos apresentados na imagem acima:

|Campo|Descrição|
|---|---|
|EPM Connection|Uma das conexões configuradas em EPM Connections|
|Filter|Nome ou parte do nome do objeto (**case sensitive**)|
|Type|Tipo do objeto|

**Exemplo:**

```python

import epmwebapi as epm
import epmprocessor as epr
import datetime

@epr.applicationMethod('GetHistoryRaw')
def get_history_raw(session, obj_dict):
    '''Get one hour raw historic data from epm dataobject'''

    endtime = session.timeEvent

    initime = endtime - datetime.timedelta(session.range)

    queryperiod = epm.QueryPeriod(initime, endtime)
     
    for obj in obj_dict.values():
        print(obj.historyReadRaw(queryperiod))

    return epr.ScopeResult(True)   
```



#### Contexto
É possível, através de um parâmetro da *session*, verificar qual é o contexto em que o método está sendo executado.

* Test - Quando executado através do botão Test do **Code Package**
* Simulation - Quando é executado a partir de em uma **Simulation**
* Production - Quando é executado a partir de em uma **Production**

Pode ser interessante criar execuções diferenciadas para cada um dos casos. Por exemplo: Em *Test* ou *Simulation* pode não ser 
interessante escrever o resultado em variáveis do **EPM Server**, mas sim mostrar o resultado utilizando `print()`.

```python
import epmprocessor as epr
import epmwebapi as epm

@epr.applicationMethod('ScopeContext')
def scope_context(session):

    if session.scopeContext == session.scopeContext.Test:
        #do it in test
        print('Test Context')

    if session.scopeContext == session.scopeContext.Simulation:
        #do it in simulation
        print('Simulation Context')

    if session.scopeContext == session.scopeContext.Production:
        #do it in production
        print('Production Context')

```

[Próxima seção - Suporte](EPMProcessorSuporte.md)

---

<sup>1</sup> O termo método advém do paradadigma de programação orientada a objetos, onde método refere-se à uma função definida em uma classe particular.

<sup>2</sup> É um termo que designa um padrão de projeto de software que permite agregar dinamicamente funcionalidades adicionais a um dado objeto.
