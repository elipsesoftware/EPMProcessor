
## EPM Processor Workbench
[Retornar ao menu](menu.md)

O **EPM Processor Workbench**, ou simplesmente *Workbench*, é a interface WEB que provê todas as funcionalidades necessárias para criação, gerenciamento, manutenção e execução de soluções implementadas em linguagem Python. 


Veja o fluxo de trabalho do **EPM Processor**:
![Fluxo epm processor](images/workbench_fluxo_processor.PNG)

### Acessando o Workbench
Qualquer máquina com acesso ao endereço e porta configurados no **EPM Processor Manager** e navegador compatível, poderá acessar a tela de autenticação.

Utilizando a porta padrão do **EPM Processor**, acesse o seguinte endereço no navegador:

http://nome_da_maquina:44338 
   

### Usuários
O **EPM Processor** autentica seus usuários junto a um **EPM Server** previamente definido como *Master*, configurado no **EPM Processor Manager**.
Qualquer usuário desse **EPM Master** poderá realizar login e acessar o *Workbench*.

Permissões de perfis de usuário:

| Perfil | Permissões  |
|---|---|
| *sa*| Tem acesso irrestrito a todos os itens.|
| Todos os demais|Tem acesso aos itens criados por ele mesmo ou aqueles que obteve permissão através de quem o criou ou do *sa*.|




### Segurança em nível de aplicativo

**Segurança de código fonte**

* Qualquer usuário terá acesso aos **Code Packages** disponíveis. 
* Para "fechar" o código fonte use o **Deploy++** para criar um **Package** e então exclua o **Code Package**.
* É de responsabilidade do usuário armazenar, fazer controle controle de versões e backups do código-fonte. 

**Segurança de Applications e Productions**

É possível definir permissões para que usuários possam ou não alterar as configurações de execução dos algoritmos.

1. Em uma **Application** ou **Solution** clique no menu Permissions
2. Na janela pode escolher o usuário e alterar as permissões Read, Write e Execute:
    * Read - Permite visualizar a configuração
    * Write - Permite editar a configuração
    * Execute - Permite iniciar e parar a execução. 

 :large_blue_diamond: Por padrão apenas o usuário *sa* e quem criou a **Application** ou **Solution** tem permissões sobre elas.

### Chave de produto

O **Workbench** mostra qual é a versão da chave de produto e o seu código. Para acessar essas informações clique no menu **About**.

[Próxima seção - EPM Connections](EPMProcessorEPMConnections.md)
