
## Code Packages
[Retornar ao menu](menu.md)

Um **Code Package** é um conjunto de códigos escritos em linguagem Python contendo as lógicas das instruções que poderão ser utilizadas posteriormente nas aplicações. O **Code Package** deverá ser "empacotado" através da operação de **Deploy** ou **Deploy++**, quando passará a ser denominado simplesmente de **Package**.

A área de visualização possui uma tabela com informações dos **Code Packages** já criados. Veja a seguir o que cada ícone representa:


|Ícone|Descrição|
|:---:|---|
|![thumbs up icon](./images/fa_up_icon_18.png)|Status da verificação de código|
|![pencil icon](./images/fa_pencil_icon_18.PNG)|Abre edição do Code Package|
|![download icon](./images/fa_download_icon_18.PNG)|Download do Code Package|
|![trash icon](./images/fa_trash_icon_18.PNG)|Exclui o Code Package|



Dentro de um **Code Package** serão feitos *uploads* e edições de códigos em linguagem Python, testar métodos e utilizar as opções de **Deploy**.

Para criar um novo **Code Package**:
1. No menu lateral direito, escolha CODE PACKAGES.
2. Na área que se abriu, clique em NEW.
3. Escolha o nome, descrição e versão.
4. O Code Package recém-criado já é aberto para edição.

:warning: *O EPM Processor não faz controle de versão de código. O gerenciamento das diferentes versões de projeto, bem como a alteração do campo *Version* fica a cargo da equipe responsável pelo desenvolvimento.*

![code package menu](images/code_packages_menus.PNG)

Os menus acima estão descritos a seguir:

|Menu|Descrição|
|---|---| 
|Edit|Abre janela para edição de nome, descrição e versão do Code Package|
|Delete|Exclui o Code Package|
|Download|d do Code Package para a máquina local|
|New Code|Insere novo algoritmo Python no Code Package|
|Add Codes|Faz upload de arquivos ou pacotes zipados de código Python|
|Compile|Verifica se existem erros de sintaxe nos códigos inseridos no Code Package|
|Deploy|Cria um Package|
|Deploy++|Cria um Package com otimização de performance e ofuscamento de código fonte.|

 :large_blue_diamond: *Para mais informações sobre a diferença de desempenho entre os pacotes gerados pela operação de **Deploy** e **Deploy++**, veja este artigo:*


#### Criando um código fonte
1. Clique em NEW CODE, escolha um nome e descrição e clique em Save.
2. Clique no nome que escolheu para abrir a edição do fonte.
3. O editor de código, com um exemplo mínimo é aberto, juntamente com um novo menu de ícones:


|Ícone|Descrição|
|:---:|---|
|![save icon](./images/fa_save_icon_18_333.png)|Salvar última edição do algoritmo|
|![refresh icon](./images/fa_refresh_icon_18_333.PNG)|Carrega última versão salva|
|![upload icon](./images/fa_upload_icon_18_333.PNG)|Faz *upload* de um código fonte e substitui o atual|
|![trash icon](./images/fa_trash_icon_18_333.PNG)|Exclui o código|
|![pencil icon](./images/fa_pencil_icon_18_333.png)|Edita nome e descrição do código|



#### Editor

No *Workbench* é disponibilizado um editor para pequenos ajustes rápidos e testes de código. Recomendamos a utilização de um editor ou IDE (*Integrated Development Environment* ou em português: Ambiente de Desenvolvimento Integrado) próprio para o desenvolvimento 
de aplicações em linguagem Python e usar o recurso de importar o código quando este já estiver testado, validado e documentado.

O editor de códigos do **EPM Processor** implementa os seguintes recursos:

* Coloração de sintaxe
* Autocompletar 
* Localizador 
* Edição em lote 
* Colapsar blocos de código (clicar na seta ao lado do número da linha)

Lista de atalhos de teclado:

|Ação|Atalho|
|---|---|
|Salvar|Ctrl+s|
|Marcar Tudo| Ctrl+a|
|Voltar|Ctrl+z|
|Avançar|Ctrl+Y|
|Edição em lote|Ctrl+Alt+k|
|Selecionar Tudo|Ctrl+A|
|Ir para linha especifica|Ctrl-L|




#### Testando um código fonte

1. Após editar o código, clique no ícone salvar
2. Clique em *Compile*
3. Escolha o método que deseja testar no *combobox Method*
4. Preencha cada campo com o tipo e valor compatíveis com seu algoritmo.
5. Clique em *Test*.
6. O resultado irá aparecer logo abaixo.

#### Criando um método Python para ser usado na estrutura do EPM Processor

A desenvolvedor de soluções para o **EPM Processor** poderá utilizar quaisquer funções e bibliotecas da linguagem Python, 
desde que a saída/resultado do código seja compatível com uma execução como serviço, ou seja, sem interface visual.

Para um método escrito em Python se tornar uma tarefa executada pelo **EPM Processor**, este deve possuir a seguinte sintaxe:

   ```python
    import epmprocessor as epr

    @epr.applicationMethod('MethodName')
    def method_name(session, param1, param2=2):
        """dosctring para documentação"""
        ...
        ...
   ```

* A primeira linha faz o *import* da biblioteca **epmprocessor**.
* A segunda linha utiliza um *decorator* da biblioteca **epmprocessor**, que deve receber um parâmetro do tipo
*string*, que será o nome do método exposto na plataforma.
* A terceira linha cria o método do usuário com os parâmetros de entrada necessários.
* A quarta linha é o *docstring* de documentação que poderá ser consultada posteriormente no *Workbench*.

Veja mais informações abaixo.

#### Documentação de métodos
O EPM Processor analisa e integra na plataforma o *docstring* de documentação dos métodos que utilizam o *decorator* **applicationMethod**.
É recomendável fazer a documentação completa dos métodos para facilitar a utilização destes.
Recomenda-se utilizar a sintaxe **reStructuredText**, padrão seguido na maioria dos projetos em linguagem Python. Desta forma, o *help* dos métodos será apresentado com uma formatação adequada à leitura por parte dos usuários destes pacotes.

 :large_blue_diamond: *Ao criar uma [**Application**](EPMProcessorApplications.md), será possível visualizar a documentação formatada caso seja adotada a sintaxe **reStructuredText**.*

Sintaxe básica de documentação:

    """ **Título do método**

    Descrição do método.
        :param1 : descrição do parâmetro
        :type param1: tipo de dado requerido pelo parâmetro
        :returns: descrição do retorno do método
        :rtype: tipo de dado de retorno do método
        :raises: em caso de exceções

    .. note::
        Nota de rodapé.

    .. todo::
        funções previstas mas ainda não implementadas no método.

    """
Para a documentação completa, acesse a página oficial da sintaxe [aqui](http://docutils.sourceforge.net/rst.html).




 
Para mais informações sobre as bibliotecas e exemplos de desenvolvimento, consulte:

* [Capítulo 10 - Algoritmos](EPMProcessorAlgoritmos.md)


#### Deploy e Deploy++


Após finalizar a criação dos algoritmos do **Code Package** é necessário fazer o procedimento de empacotamento.


* Criar um **Package** com **Deploy** faz com que este mantenha os códigos-fonte legíveis. Permitindo que o desenvolvedor faça entregas de fontes abertos. Ideal para os casos onde se deseja que os usuários destes pacotes possam ter acesso ao código, seja para uma maior compreensão dos algoritmos implementados, seja para eventuais manutenções e/ou expansões dos mesmos.
* Criar um **Package** com **Deploy++** faz com que o **EPM Processor** crie binários de alto desempenho. Neste caso o código fonte é convertido em binário utilizando o módulo *Cython*. Empacotamentos desta forma, além de maior desempenho nas execuções, ainda conferem uma maior segurança da codificação decorrente do próprio processo de compilação, além de proporcionar uma proteção da propriedade intelectual. Para sistemas em produção, recomendamos a utilização desse método. 

 :warning: *Uma vez que o código tenha passado pelo processo de **Deploy++**, é impossível recuperar
o código fonte original. Recomendamos adotar um sistema de controle de verãos dos códigos fonte, como por exemplo: Git, Mercurial, SVN, dentre outros.* 

Para fazer o empacotamento:

1. Clique no ícone Salvar ou pressione Ctrl+s
2. Clique em Compile
3. Clique em Deploy ou Deploy++

![imagem deploy code package](./images/code_packages_deploy.png)

A tabela a seguir detalha os campos disponíveis nessa janela:

|Campo|Descrição|
|---|---|
|Name|Nome do Package que será criado. O padrão é manter o nome do Code Package|
|Edit Name|Deve ser marcado se for necessário editar o campo Name|
|Description|Descrição do Package|
|Version|Versão do Package|
|Force Override Package|Sobrescreve um Package que já tenha sido criado com o mesmo nome|



4. Preencha os campos e clique em Deploy para finalizar o procedimento.


[Próxima seção - Packages](EPMProcessorPackages.md)








