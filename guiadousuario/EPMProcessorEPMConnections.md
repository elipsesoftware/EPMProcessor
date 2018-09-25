
## EPM Connections
[Retornar ao menu](menu.md)

Uma **EPM Connection** é uma configuração de conexão a um **EPM Webserver** que, por sua vez, está vinculado a um único **EPM Server**. Através desta conexão é que torna-se possível o acesso aos seguintes itens de um **EPM Server** correspondente:

* Eventos (utilizados para disparar a execução automática de **Produtcions**)
* Data Objects (objetos de dados do **EPM Server**)
* Estrutura de Dados(organização hierárquica dos dados no **EPM Server**, pode ser através de diretórios ou modelagem de objetos do Elipse E3 ou Elipse Power)

O **EPM Processor** permite múltiplas **EPM Connections**, seja para um mesmo servidor, ou servidores distintos.

Para criar uma **EPM Connection** siga estes procedimentos:
1. No menu lateral clique em **EPM Connections** para abrir a seção.
2. Clique em **NEW**
3. Preencha os campos conforme as configurações do seu ambiente e clique em Save para finalizar.

![new epm connection](images/connections_new_epm_connection.png)

Os campos disponíveis nesta janela estão descritos a seguir:

| Campo  | Descrição  |
|---|---|
| Name  |Nome da nova EPM Connection | 
| Address  | Nome ou IP da máquina onde está instalado o EPM Webserver  |
| Authentication Server  | Endereço http da máquina onde está instalado o EPM Webserver seguido da porta configurada no campo **Authentication Port** da configuração do EPM Webserver(Default: 44333). Exemplo: **http://nome_maquina:44333** | 
| Web Api|Endereço http da máquina onde está instalado o EPM Webserver seguido da porta configurada no campo **Web Api Port** da configuração do EPM Webserver(Default:44332). Exemplo: **http://nome_maquina:44332**|
| User Name| Nome do usuário |
| Password | Senha do usuário|

[Próxima seção - Resources](EPMProcessorResources.md)
