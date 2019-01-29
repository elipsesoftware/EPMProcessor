# Resources

*[Retornar ao menu](README.md)*

A seção **Resources** dá acesso à estrutura de pastas e arquivos disponível no **EPM Webserver**. Nesta estrutura é possível dispor todos os arquivos que possam ser necessários para uso nas aplicações, como por exemplo arquivos de modelos de processo para usar em simulações ou predições, arquivos com _templates_ para usar na produção de relatórios, imagens, dados, etc.

Além de seu próprio diretório, o **EPM Processor** tem acesso ao diretório do **EPM Portal**, viabilizando relatórios e outros arquivos para serem consumidos nesta outra plataforma.

Os **Resources** são acessíveis também pela API, permitindo ações de escrita, leitura, atualização e exclusão de arquivos e diretórios.

> + Estes diretórios são virtuais, não acessíveis através do sistema de arquivos do sistema operacional.

Para acessar esta estrutura, siga estes procedimentos.

1. No menu lateral, clique em **Resources**.
2. Navegue pela estrutura utilizando a opçao ![expand](./images/fa_chevron_icon.png "Expandir").

As opções de arquivos e diretórios estão descritas na tabela a seguir.

|Opção|Descrição|
|:---:|---|
|![pencil icon](./images/fa_pencil_icon_18.png "Editar")|Permite editar o nome e a descrição|
|![cloudupload icon](./images/fa_cloudupload_icon_18.png "Upload")|Executa o *upload* de um arquivo|
|![plus icon](./images/fa_plus_icon_18.png "Inserir")|Insere um novo diretório|
|![refresh icon](./images/fa_refresh_icon_18.png "Recarregar")|Recarrega um diretório|
|![trash icon](./images/fa_trash_icon_18.png "Apagar")|Apaga um diretório ou arquivo|

> + Os arquivos inseridos através desta ferramenta são salvos em formato binário no servidor. Ao acessá-los via código, lembre-se de convertê-los, se necessário.

## Permissões

|Tipo|Permissão|
|---|---|
|Escrita|Usuário que inseriu o **Resource** mais o usuário **sa**|
|Leitura|Todos os usuários|

*[Próxima Seção: Code Packages](EPMProcessorCodePackages.md)*
