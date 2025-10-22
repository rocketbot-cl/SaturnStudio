# Saturn Studio
  
Este módulo te permite conectarte a tu cuenta de Saturn Studio y gestionar tus flujos de trabajo.  

*Read this in other languages: [English](Manual_SaturnStudio.md), [Português](Manual_SaturnStudio.pr.md), [Español](Manual_SaturnStudio.es.md)*
  
![banner](imgs/Banner_SaturnStudio.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar
  
Conectar tu cuenta de Saturn Studio usando tu API Key.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|API Key de Saturn Studio|eyJhbGciOi...|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Ejecutar workflow
  
Ejecutar un workflow desde tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Workflow URL|URL del flujo de trabajo en Saturn Studio|https://studio.rocketbot.com/flow?d=xxxx&i=yyyy&r=e|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|
