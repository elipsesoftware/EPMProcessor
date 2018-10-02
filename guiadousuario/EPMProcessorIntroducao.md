# Introdução

*[Retornar ao menu](menu.md)*

## Sobre o EPM Processor

O **EPM Processor** é um módulo que se integra à plataforma **Elipse Plant Manager** (EPM). Através desta plataforma é possível coletar dados de diversas origens, armazená-los e contextualizá-los, oferecendo alto desempenho de gravação e consulta, além de inúmeras ferramentas para visualização e análises a fim de agilizar o processo de extração de conhecimento e no balizamento de tomadas de decisões.

O **EPM Processor** atua neste cenário possibilitando que algoritmos escritos em linguagem **Python** sejam colocados em execução automatizada ou sob demanda. As execuções automáticas são baseadas em eventos e disponibilizam conexões nativas aos dados de processo de um ou mais **EPM Servers**. Alguns casos típicos de uso desta ferramenta são cálculos de indicadores de desempenho, inferências sobre variáveis de processo, cálculos de previsões de demandas, geração de relatórios e documentações automáticas ou sob demanda, dentre outros.

Com esta ferramenta é possível gerenciar toda a geração de informações baseadas nos dados de processo, incorporando ou não informações de outras fontes de dados, tudo em um ambiente seguro e de fácil manutenção, requisitos vitais para a gestão das informações do negócio.

## Chave de Produto

Existem quatro configurações do módulo **EPM Processor**, descritas na tabela a seguir.

|Configuração|Processos|Productions Simultâneas|
|---|---|---|
|**EPM Processor Demo**|4+|10|
|**EPM Processor Lite**|1|100|
|**EPM Processor Enterprise**|4|1000|
|**EPM Processor Full**|4+|1000+|

+ **Processos**: Processos do interpretador **Python** em execução no sistema operacional.
+ **Productions**: Cada **Production** corresponde a uma aplicação configurada para execução automática segundo eventos produzidos em tempo real.
+ No caso do **EPM Server** definido como _Master_ estar executando em modo de demonstração (**Demo**), o **EPM Processor** automaticamente entra em modo de demonstração também.


É importante ressaltar que, uma vez selecionado o tipo de configuração do módulo, todas as chaves de produto do **EPM Processor** adquiridas correspondem a este mesmo tipo. Por exemplo, é possível adquirir três chaves de produto do módulo **EPM Processor** para o tipo *Lite* de configuração. Ao adquirir uma quarta chave de produto, esta necessariamente também corresponde ao tipo *Lite*, a não ser que seja realizado o _upgrade_ de tipo, quando todas as chaves de produto passam a corresponder ao novo tipo de configuração.

As chaves de produto do módulo **EPM Processor** são contabilizadas no momento em que um **EPM Processor** se registra e estabelece uma conexão com um **EPM Server** definido como _Master_ que, por sua vez, verifica nas suas configurações de produto quantos módulos de **EPM Processor** são aceitos e estão disponíveis naquele momento. No caso de não haver mais chaves de produto de **EPM Processor** disponíveis, os módulos do **EPM Processor** que tentarem se conectar ao **EPM Server** definido como _Master_ têm sua conexão negada.

A partir da versão 3.06 do sistema **EPM**, o **EPM Processor** possui uma versão para avaliação, ou seja, uma chave de produto para o modo **Demo**. O primeiro **EPM Processor** que se registrar e tentar estabelecer uma conexão com o **EPM Server** definido como _Master_ é aceito, porém opera em modo de demonstração (**Demo**). Desta forma é possível avaliar os benefícios que o **EPM Processor** pode trazer para um ambiente onde já exista um **EPM Server** em operação.

Para mais informações, entre em contato com o setor comercial da *[Elipse Software](https://www.elipse.com.br)*.

## EPM Master

O **EPM Processor** pode receber dados de diversos **EPM Servers**. Neste caso, deve ser selecionado um **EPM Server** para ser o _Master_ do **EPM Processor**. Este servidor é responsável pelas chaves do produto e pela autenticação de usuários.

![arquitetura 2 epm 1 processor](./images/arquitetura_2epm_1processor.PNG "Arquitetura com um EPM Processor e vários EPM Servers")

Outra opção é ter vários **EPM Processors** para um único **EPM Server**. Neste caso, o **EPM Server** deve ter as chaves de produto para o número de **EPM Processors** instalados.

![arquitetura 2 epm 1 processor](./images/arquitetura_1epm_2processor.PNG "Arquitetura com vários EPM Processors e um EPM Server")

*[Próxima Seção: Instalação](EPMProcessorInstalacao.md)*
