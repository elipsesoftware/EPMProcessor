# EPM Processor - Terminologia


[Retornar ao menu](menu.md)

Lista organizada em ordem alfabética. Contém a descrição de diversos termos utilizados neste manual. 


#### Application

Configuração básica para a execução de um método.
As *Applications* são organizadas em grupos para facilitar sua localização e gerenciamento, consistindo basicamente nas definições de valores padrões para os parâmetros do método ao qual representa. Mais informações podem ser obtidas diretamente no tópico [Applications](EPMProcessorApplications.md).


#### Application Method

Corresponde à implementação em linguagem Python de uma função identificada através de um *decorator* como sendo um método passível de execução de uma *Application*.


#### Code Package

Corresponde a um conjunto de códigos escritos em linguagem Python contendo as instruções que poderão ser utilizadas posteriormente nas aplicações.
O *Code Package* deverá ser "empacotado" através da operação de *Deploy* ou *Deploy++*, quando passará a ser denominado simplesmente de *Package*. Mais informações podem ser obtidas diretamente no tópico [Code Packages](EPMProcessorCodePackages.md).


#### Deploy

É a operação de empacotamento de um *Code Package*, criando um *Package*. Mais informações podem ser obtidas diretamente no tópico [CodePck/Deploy](EPMProcessorCodePackages.md#deploy-e-deploy).


#### Deploy++

É a operação de empacotamento de um *Code Package* gerando um *Package* binário, com maior desempenho nas execuções. Mais informações podem ser obtidas diretamente no tópico [CodePck/Deploy](EPMProcessorCodePackages.md#deploy-e-deploy).


#### EPM Master

Corresponde ao *EPM Server* responsável pelas chaves do produto e autenticação de usuários.


#### epmwebapi

Biblioteca Python para interação com objetos e dados de um *EPM Server*.


#### Method

Ver [Application Method](EpmProcessorTerminologia.md#application-method)


#### Numpy

Biblioteca Python para computação científica, especialmente que envolvam cálculos e manipulações matriciais. Mais informações podem ser obtidas diretamente no site do módulo [Numpy](http://www.numpy.org).


#### Package

É o resultado da operação de empacotamento de um *Code Package* para posterior utilização em uma *Application*. Mais informações podem ser obtidas diretamente no tópico [CodePackage/Deploy](EPMProcessorCodePackages.md#deploy-e-deploy).



#### Pandas

Biblioteca Python que agiliza o processo de análises sobre de dados tabulares. Mais informações podem ser obtidas diretamente no site do módulo [Pandas](https://pandas.pydata.org).


#### Production

É a designação para uma aplicação que pode ser colocada em modo de produção, ou seja, em estado para avaliação toda vez que o evento associado a ela seja disparado. Mais informações podem ser obtidas diretamente no tópico [Criando Productions](EPMProcessorSolutions.md#criando-productions).


#### Python

Linguagem de programação utilizada para a codificação das lógicas utilizadas nas *Solutions*. Mais informações podem ser obtidas diretamente no site [Python](https://www.python.org).


#### Resources

Repositório de arquivos do *EPM Processor* e *EPM Portal*. Mais informações podem ser obtidas diretamente no tópico [Resources](EPMProcessorResources.md).


#### Scikit-learn

Biblioteca Python para aplicações de Machine Learning. Mais informações podem ser obtidas diretamente no site [Scikit-learn](http://scikit-learn.org).


#### Scipy

Biblioteca Python para computação científica (otimizações, estatística, cálculo numérico, álgebra linear, etc.). Mais informações podem ser obtidas diretamente no site [Scipy](https://www.scipy.org).


#### Session

Parâmetro de entrada que contém diversas informações relativas a execução de uma *Production*. Mais informações podem ser obtidas diretamente no tópico [Biblioteca do EPM Processor](EPMProcessorBibliotecaepmprocessor.md).


#### Simulation

É a designação para uma aplicação configurada para simulações, ou seja, para avaliações segundo eventos simulados, sejam eles passados ou futuros. Mais informações podem ser obtidas diretamente no tópico [Criando Simulations](EPMProcessorSolutions.md#criando-simulations).


#### Solution

É uma agrupamento que serve para organizar as soluções implementadas sobre as *Applications*, seja para colocar em produção ou simulação. Mais informações podem ser obtidas diretamente no tópico [Solutions](EPMProcessorSolutions.md).


#### Workbench

Interface Web de uso geral do *EPM Processor*. Mais informações podem ser obtidas diretamente no tópico [Workbench](EPMProcessorWorkbench.md).




