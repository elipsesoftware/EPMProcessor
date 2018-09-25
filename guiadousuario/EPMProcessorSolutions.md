## Solutions

[Retornar ao menu](menu.md)

As **Solutions** são agrupamentos que servem para organizar as soluções implementadas sobre aplicações, que podem ser colocadas em produção (eventos em tempo real) ou simuladas (eventos simulados e execução sob demanda). Desta forma, para melhor gerenciar as execuções das **Solutions**, elas foram divididas em dois grupos:

* **Simulation** - São gerados eventos simulados e a aplicação pode ser executada em diferentes períodos de tempo. Por exemplo: Rodar uma dada aplicação para cada um dos últimos 12 meses.

* **Production** - Os eventos que iniciarão a execução de uma dada aplicação são gerados em tempo real a partir de um **EPM Server**. Por exemplo: O método rodará todo dia 01 do mês às 00:01.

A criação e configuração dos eventos de um dado **EPM Server** é toda realizada, monitorada e gerenciada a partir do **EPM Studio**. Veja a seção **EPM Events** no manual do EPM para mais informações.

Para visualizar e criar novas **Solutions**:

1. No menu lateral clique em **Solutions**.
2. Será mostrada a lista de **Solutions** disponíveis.

Os ícones da lista possuem as seguintes funções:


|Ícone|Descrição|
|:---:|---|
|![pencil icon](./images/fa_pencil_icon_18.PNG)|Edita a Solution|
|![copy icon](./images/fa_copy_icon_18.png)|Cria uma cópia com nome diferente|
|![trash icon](./images/fa_trash_icon_18.png)|Exclui a Solution|

3. Clique em New.
4. Escolha o nome e a descrição da Solution.
5. Para editar a Solution clique no ícone "lápis".
6. O sumário da **Solution** é mostrado. 

O menu da **Solution** possui os itens *Edit*, *Delete* e *Permissions*. Este menu tem as mesmas funções da **Application**.

Também são mostrados os menus **New** e **View All** para **Simulations** e **Productions**. Através destes é possível, respectivamente, criar um novo ou visualizar a lista itens disponíveis.


### Criando Simulations

Para criar uma nova **Simulation**:

1. Na visualização de Simulations clique em New.

![new simulation](./images/solutions_new_simulation.png)

A tabela a seguir descreve os itens da janela acima.

|Item| Descrição|
|---|---|
|Name|Nome da Simulation|
|Solution|A qual Solution a nova Simulation deverá pertencer|
|Application Groups|Em qual Application Group se encontra a Application requerida|
|Application|Qual Application deverá ser colocada na Simulation|
|Start|Data/hora de ínicio da simulação|
|End|Data/hora do fim da simulação|
|Count|Intervalo de execução, relacionado a Unit|
|Unit|Unidade do Intervalo de execução|
|Is Period| Se marcado, executa o método somente em data/horas específicas definidos nos campos abaixo|
|Select Date and Time|Seleciona uma data e hora no calendário|
|Add to Dates|Inclui o data/hora selecionada na sequência de execuções|
|Execute in Dates|Data/hora em que a simulação será executada|

* Exemplo de configuração: 

 ![exemplo de configuracao](./images/solutions_simulation_example.PNG)
 
 Na configuração acima, serão gerados 30 eventos. Pois o intervalo é de 30 dias, e a unidade e contagem é 1 dia.


2. Clique em Save.
3. Na lista de Simulations, clique no ícone "lápis" para abrir a visualização.
4. Clique no Botão Execute para iniciar a execução do método.
5. Aguarde o término para ver o resultado.


### Criando Productions

Para criar uma nova **Production**:

1. Na visualização de Productions clique em New.

![new simulation](./images/solutions_new_production.png)

A tabela a seguir descreve os itens da janela acima.

|Item| Descrição|
|---|---|
|Name|Nome da Production|
|Solution|A qual Solution a nova Production deverá pertencer|
|Application Groups|Em qual Application Group se encontra a Application requerida|
|Application|Qual Application deverá ser colocada na Production|
|Connections|Connection com o EPM Server da qual se deseja utilizar o evento|
|Events|Nome do evento utilizado para disparar a execução do algoritmo|
|Enable Retries on Erros|Se marcado, habilita as retentativas de execução em caso de erro|
|Abort Retries on new Event|Se marcado, não faz retentativas da execução anterior se um evento novo ocorreu|
|Retries| Número de retentativas em caso de erro|
|Wait Time|Intervalo de tempo entre as retentativas|

2. Preencha os campos conforme a necessidade.
3. Clique em Save.

#### Visualizando e editando Productions

Para abrir a visualização e edição de **Productions**

1. No menu lateral esquerdo clique em **Solutions**.
2. Clique no ícone "Lápis" para abrir a Solution desejada.
3. Na seção de Productions clique em **View All**.

A tabela abaixo detalha cada um dos ícones disponíveis na tabela.



|Ícone|Descrição|
|:---:|---|
|![pencil icon](./images/fa_pencil_icon_18.PNG)|Abre a visualização e edição da Production|
|![copy icon](./images/fa_copy_icon_18.png)|Cria uma cópia com nome diferente|
|![trash icon](./images/fa_trash_icon_18.png)|Exclui a Production|
|![play icon](./images/fa_play_icon_18.png)|Inicia ou para a execução|


4. Clique no ícone "lápis" para abrir a visualização da **Production**.

Essa visualização possui quatro abas:

* **Results** - Visualização do resultado da execução da **Production**. Filtro por data para localizar o resultado de execuções.
* **App Config** - Edição da **Production** em relação a **Application**. É possível alterar os valores "padrão" inseridos na configuração da **Application**.
* **Execution Config** - Permite alterar o evento que dispara a execução da **Production** e configurar as retentativas em caso de erro.
* **Statistics** - Estatísticas gerais de execução. Veja a tabela a seguir:

|Valor|Descrição|
|---|----|
|Min Exec. Time|Menor tempo de execução do método|
|Max Exec. Time|Maior tempo de execução do método|
|Average Exec. Time| Média de tempo de execução dos métodos|
|Standard Deviation Exec. Time| Desvio padrão de tempo de execução dos métodos|
|Total Executions|Quantidade total de execuções|
|Total Fails|Quantidade total de execuções com falha|
|Retries Count| Quantidade total de retentativas |
|Status Last Execution| Status da última execução| 
|Last State Change| Última alteração na configuração| 


[Próxima seção - Algoritmos](EPMProcessorAlgoritmos.md)
