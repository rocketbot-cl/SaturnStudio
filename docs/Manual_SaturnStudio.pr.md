



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
