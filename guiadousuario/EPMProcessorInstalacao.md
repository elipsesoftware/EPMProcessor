
## Instalação
[Retornar ao menu](menu.md)

### Pré-requisitos
* Windows 7 SP1 ou superior x64
* Windows Server 2008 R2 SP1 ou superior
* .NET 4.7.1 ou superior
* IIS com CGI ativado (veja a sessão [Perguntas Frequentes](EPMProcessorSuporte.md#perguntas-frequentes))
* EPM Server 3.6 ou superior
* EPM Webserver 1.0 ou superior ([instalação](EPMWebserver.md))
* Navegadores Firefox ou Chrome
* Python 3.6 x64 - Instalar com a opção ***install for all users***.
  * Instalação do [Anaconda3](Anaconda.md) (Inclui o Python e diversos pacotes)
  * Instalação do [Python](Python.md) (Somente o interpretador)
  * O instalador irá instalar as bibliotecas automaticamente via *Pypi*. Se a máquina estiver offline, 
  instale manualmente usando a lista de requerimentos (veja a sessão [Perguntas Frequentes](EPMProcessorSuporte.md#perguntas-frequentes)).  
* 1.5 GB de espaço em disco para o download e instalação.



### Hardware
O *hardware* necessário para o **EPM Processor** irá depender da complexidade das tarefas, número de execuções e deve ser pensado para os períodos de picos de utilização. Considere aumentar a capacidade quando perceber que o tempo de execução dos algoritmos está impactando de forma negativa a solução.


:bulb: As configurações de produto tem influência na capacidade de processamento. Verifique as opções com o setor comercial.

 
   
### Download 

Faça o *download* no site da Elipse, na seção do produto **Elipse Plant Manager**.

http://www.elipse.com.br/downloads

### Interpretador Python
O **EPM Processor** necessita de uma versão 3.6 X64 ou superior do interpretador Python padrão(CPython). Fica a escolha do usuário a distribuição. Recomendamos:

* Em ambiente de desenvolvimento instalar a distribuição Anaconda, pois já possui todas as principais bibliotecas para projetos de ciência de dados.
* Em ambientes de produção instalar o interpretador disponível em Python.org, e instalar somente as bibliotecas utilizadas no projeto.

 

### Instalação

1. Tenha certeza de que seu ambiente atende os requisito listados acima.
2. Se houver alguma execução do Python em andamento, termine-a.
2. Execute o instalador do **EPM Processor** em Modo Administrador: Clique com o botão direito no arquivo **epmprocessor-enu.exe** e escolha a opção Executar como Administrador. 
3. Aceite os termos de utilização do produto.
4. Escolha o diretório de instalação do **EPM Processor**.
5. Escolha o diretório de instalação do MongoDB*.
6. Informe ao instalador o diretório de instalação do Python. 
7. Aguarde o término da instalação.

:warning: *Todos os registros e configurações do EPM Processor ficarão salvos no MongoDB. Faça backups periódicos para evitar a perda da aplicação em caso de problemas físicos no servidor, ou erros de procedimento com os arquivos (Exclusão, alteração, etc).  

#### Instalação em ambientes virtualizados 

Informe ao setor comercial da Elipse Software sempre que estiver utilizando ambiente virtualizado, redundância de VM(HA ou FT) ou os servidores não possuírem uma porta USB. A Elipse disponibiliza chave de software especial para esses casos.


### Upgrade de versão

Recomendamos que mantenha a versão sempre atualizada. Empresas que aderem ao programa **Elipse Care** possuem upgrade gratuito da chave. 
Antes de instalar uma versão superior, verifique se a chave está apta a receber esta versão.
 
Antes de instalar uma nova versão, faça a desinstalação via Painel de Controle.

:warning: Não exclua nenhuma pasta do diretório de instalação do **EPM Processor manualmente**, caso isso ocorra perderá suas configurações.



Faça esse procedimento de forma planejada, pois durante este processo, nenhuma **Solution** poderá ser executada.

### Desinstalação
Faça a desinstalação do **EPM Processor** via Painel de Controle.
  
### EPM Processor Manager
O **EPM Processor Manager** é a interface de gerenciamento das conexões, portas, etc.
1. Para abrir o menu, clique com o botão direito no ícone do **EPM Processor Manager**.


![EPM Processor Manager](images/instalacao_menu_manager.PNG)

Os campos disponíveis neste menu estão descritos a seguir:

| Campo  | Descrição  |
|---|---|
| About EPM Processor | Abre tela com informações de versão e Copyright |
| Open EPM Processor | Abre o endereço http://localhost:porta no navegador padrão do sistema operacional|
| Settings| Abre janela de configuração| 
| Diagnostic| Abre janela para visualização de informações sobre o funcionamento do EPM Processor|
| Errors List|Abre janela para visualização de erros em serviços e permissões.|
| Start EPM Processor|Inicia os serviços do EPM Processor|
| Shutdown EPM Processor|Para os serviços do EPM Processor|
| Restart EPM Processor|Reinicia os serviços do EPM Processor|
| Close Manager|Fecha o EPM Processor Manager|


#### Configurações
1. Para abrir as configurações do **EPM Processor Manager**, escolha a opção *Settings* do menu.

  ![Manager Settings](./images/instalacao_manager_general_settings.png)
  
 Os campos disponíveis na aba *General* estão descritos a seguir:

| Campo  | Descrição  |
|---|---|
| Master User Admin | Usuário do EPM *Master* |
| Master User Admin Password|Senha do EPM *Master*|
| Authentication Port|Porta do serviço de autenticação do EPMWebserver. Deve ser utilizada a mesma configurada no EPM Webserver. **Padrão:44333**|
| Web Api Port|Porta da API do EPMWebserver. Deve ser utilizada a mesma configurada no EPM Webserver. **Padrão:44332**|
| EPM Processor Workbench|Porta para o acesso do Workbench. Essa porta deverá ser usada para acesso ao Workbench via navegador. **Padrão:44338**|

 Os campos disponíveis na aba **EPM *Master*** estão descritos a seguir:

| Campo  | Descrição  |
|---|---|
| EPM Python Engine| Porta para acesso ao serviço Python Engine. \*Não deve ser alterada por motivos não explícitos. |
| EPM Processor Engine|Porta para acesso ao serviço Processor Engine. \*Não deve ser alterada por motivos não explícitos.|
  
  Os campos disponíveis na aba Manager estão descritos a seguir:

| Campo  | Descrição  |
|---|---|
| Send an email| Habilita o envio de email para o caso existência de erros na execução do EPM Processor|
| SMTP Server| Endereço do servidor SMTP|
| User |Nome de usuário da conta de email|
| Password|Senha da conta de email|
|Port|Porta do servidor SMTP|
|SSL|Marcar se o servidor utiliza SSL|
|From|Endereço de email do remetente|
|To|Endereço de email do destino| 

 :large_blue_diamond: 10 minutos após a inicialização do **EPM Processor Manager**,
  se a opção **Send an email** estiver marcada e houver alguma falha ativa, um email é enviado. Uma nova verificação e envio é feita
  a cada 24 horas. Em caso de falha no envio, haverão 3 tentativas em um período de 10 minutos cada.  

#### Diagnósticos

1. Para abrir a visualização do diagnóstico do **EPM Processor**, escolha a opção *Diagnostic* no menu.

  Os menus disponíveis nesta janela estão descritos a seguir:

| Menu  | Descrição  |
|---|---|
| Windows Services- General| Informações sobre o funcionamento dos serviços relativos ao EPM Processor |
| Python - General|Informações sobre a instalação do Python utilizada pelo EPM Processor|
| Python - Modules|Módulos Python instalados. Ao clicar no botão **Export requirement** é gerado o arquivo Requirements.txt.|
| Python - EPM Modules| Informações sobre os módulos Python do EPM instalados|
| EPM Packages - General|Packages de usuário disponíveis no EPM Processor|

[Próxima seção - Workbench](EPMProcessorWorkbench.md)

 
