# EPM Processor: Terminologia

*[Retornar ao menu](README.md)*

Este tópico contém uma lista, em ordem alfabética, com a descrição de diversos termos utilizados neste Manual.

## Application

Configuração básica para a execução de um método. As **Applications** são organizadas em grupos para facilitar sua localização e gerenciamento, consistindo basicamente nas definições de valores padrão para os parâmetros do método que representam. Consulte o tópico *[Applications](EPMProcessorApplications.md)* para mais informações.

## Application Method

Corresponde à implementação em linguagem **Python** de uma função, identificada através de um _decorator_, como sendo um método passível de execução de uma **Application**.

## Code Package

Corresponde a um conjunto de códigos escritos em linguagem **Python** contendo as instruções que podem ser utilizadas posteriormente nas aplicações. Um **Code Package** deve ser empacotado através das operações de **Deploy** ou **Deploy++**, quando passa a ser denominado simplesmente de **Package**. Consulte o tópico *[Code Packages](EPMProcessorCodePackages.md)* para mais informações.

## Deploy

É a operação de empacotamento de um **Code Package** para criar um **Package**. Consulte o tópico *[Code Packages - Deploy e Deploy++](EPMProcessorCodePackages.md#deploy-e-deploy-)* para mais informações.

## Deploy++

É a operação de empacotamento de um **Code Package** para gerar um **Package** binário, com maior desempenho nas execuções. Consulte o tópico *[Code Packages - Deploy e Deploy++](EPMProcessorCodePackages.md#deploy-e-deploy-)* para mais informações.

## EPM Master

Corresponde ao **EPM Server** responsável pelas chaves de produto e pela autenticação de usuários.

## epmwebapi

Biblioteca em linguagem **Python** para interação com objetos e dados de um **EPM Server**.

## Method

Consulte o item *[Application Method](EpmProcessorTerminologia.md#application-method)*.

## Numpy

Biblioteca em linguagem **Python** para computação científica, especialmente que envolva cálculos e manipulações matriciais. Consulte a página da *[Biblioteca](https://www.numpy.org)* para mais informações.

## Package

É o resultado da operação de empacotamento de um **Code Package** para posterior utilização em uma **Application**. Consulte o tópico *[CodePackage - Deploy e Deploy++](EPMProcessorCodePackages.md#deploy-e-deploy)* para mais informações.

## Pandas

Biblioteca em linguagem **Python** que agiliza o processo de análise sobre dados tabulares. Consulte a página da *[Biblioteca](https://pandas.pydata.org)* para mais informações.

## Production

É a designação para uma aplicação que pode ser colocada em modo de produção, ou seja, pode ser colocada em um estado para avaliação toda vez que o evento associado seja disparado. Consulte o tópico *[Criando Productions](EPMProcessorSolutions.md#criando-productions)* para mais informações.

## Python

Linguagem de programação utilizada para a codificação das lógicas utilizadas nas **Solutions**. Consulte a página da *[Linguagem Python](https://www.python.org)* para mais informações.

## Resources

Repositório de arquivos do **EPM Processor** e do **EPM Portal**. Consulte o tópico *[Resources](EPMProcessorResources.md)* para mais informações.

## Scikit-learn

Biblioteca em linguagem **Python** para aplicações de _Machine Learning_. Consulte a página da *[Biblioteca](http://scikit-learn.org)* para mais informações.

## Scipy

Biblioteca em linguagem **Python** para computação científica (otimizações, estatística, cálculo numérico, álgebra linear, etc.). Consulte a página da *[Biblioteca](https://www.scipy.org)* para mais informações.

## Session

Parâmetro de entrada que contém diversas informações relativas à execução de uma **Production**. Consulte o tópico *[Criando Algoritmos para o EPM Processor - Parâmetros de um Método](EPMProcessorAlgoritmos.md#par-metros-de-um-m-todo)* para mais informações.

## Simulation

É a designação para uma aplicação configurada para simulações, ou seja, para avaliações segundo eventos simulados, sejam eles passados ou futuros. Consulte o tópico *[Criando Simulations](EPMProcessorSolutions.md#criando-simulations)* para mais informações.

## Solution

É uma agrupamento que serve para organizar as soluções implementadas sobre as **Applications**, seja para colocar em produção ou em simulação. Consulte o tópico *[Solutions](EPMProcessorSolutions.md)* para mais informações.

## Workbench

Interface _web_ de uso geral do **EPM Processor**. Consulte o tópico *[Workbench](EPMProcessorWorkbench.md)* para mais informações.
