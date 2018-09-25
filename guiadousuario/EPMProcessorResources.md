
## Resources
[Retornar ao menu](menu.md)

A seção **Resources** dá acesso a estrutura de pastas e arquivos disponibilizada pelo **EPM Webserver**. Nela é possível dispor todos os arquivos que possam ser necessários para uso nas aplicações, como por exemplo arquivos de modelos de processo para usar em simulações/predições, arquivos com templates para usar na produção de relatórios, imagens, dados, etc.

Além de seu próprio diretório, o **EPM Processor** tem acesso ao diretório do **EPM Portal**, viabilizando a disponibilização de relatórios e/ou outros arquivos para serem consumidos nessa outra plataforma.

Os **Resources** são acessíveis também pela API, permitindo ações de escrita, leitura, atualização e exclusão de arquivos e diretórios.

 :large_blue_diamond: Esses diretórios são virtuais, não sendo acessíveis através do sistema de arquivos do sistema operacional.

Para acessar essa estrutura
1. No menu lateral clique em **Resources**.
2. Navegue pela estrutura através do botão **>**
 
Os ícones ao lado de arquivos e diretórios possuem as seguintes funções:

|Ícone|Descrição|
|:---:|---|
|![pencil icon](./images/fa_pencil_icon_18.PNG)|Editar nome e descrição|
|![cloudupload icon](./images/fa_cloudupload_icon_18.png)|Fazer *upload*  de um arquivo|
|![plus icon](./images/fa_plus_icon_18.PNG)|Inserir novo diretório|
|![refresh icon](./images/fa_refresh_icon_18.PNG)|Recarregar diretório|
|![trash icon](./images/fa_trash_icon_18.png)|Deleta diretório ou arquivo|

:warning: Os arquivos inseridos através dessa ferramenta, ficam salvos de forma binéria no servidor. Ao acessá-los via codigo, lembre de fazer a conversão, se necessário. 

### Permissões

|Tipo|Permissão|
|---|---|
|Escrita| Usuário que inseriu o resource + Usuário *sa*|
|Leitura|Todos os usuários|


[Próxima seção - Code Packages](EPMProcessorCodePackages.md)
