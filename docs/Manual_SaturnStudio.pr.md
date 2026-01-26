



# Saturn Studio
  
Este módulo permite que você se conecte à sua conta Saturn Studio e gerencie seus fluxos de trabalho.  

*Read this in other languages: [English](Manual_SaturnStudio.md), [Português](Manual_SaturnStudio.pr.md), [Español](Manual_SaturnStudio.es.md)*
  
![banner](imgs/Banner_SaturnStudio.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar
  
Conectar com Saturn Studio usando sua API Key.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|API Key|API Key para Saturn Studio|eyJhbGciOi...|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Executar workflow
  
Executar um fluxo de trabalho na sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Workflow URL|Workflow URL para Saturn Studio|https://studio.rocketbot.com/flow?d=xxxx&i=yyyy&r=e|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Carregar arquivo para o File Storage
  
Carregue um arquivo para o File Storage da sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do Arquivo|Caminho do arquivo a ser carregado|C:/Users/User/Downloads/file.file|
|Atribuir resultado a variável|Nome da variável onde o resultado será armazenado|Variável|

### Listar todos os arquivos no File Storage
  
Retorna uma lista com todos os arquivos no File Storage da sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Retorna uma lista com todos os arquivos no File Storage da sua conta do Saturn Studio|Variável|

### Excluir um arquivo do File Storage
  
Exclui um arquivo do File Storage da sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do arquivo|ID do arquivo a ser excluído no File Storage da sua conta do Saturn Studio|Arquivo|
|Atribuir resultado a variável|Nome da variável onde o resultado será armazenado|Variável|

### Listar todos os robôs no Saturn Studio
  
Retorna uma lista com todos os robôs da sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Retorna uma lista com todos os robôs da sua conta do Saturn Studio|Variável|
|Filtrar robôs ativos|Marque para listar apenas os robôs ativos|True|

### Parar todos os robôs em execução
  
Para todos os robôs em execução na sua conta do Saturn Studio.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Variável onde o resultado da desativação dos robôs será armazenado|Variável|
