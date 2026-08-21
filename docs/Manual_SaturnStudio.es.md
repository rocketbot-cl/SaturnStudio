



# Saturn Studio

Este módulo te permite conectarte a tu cuenta de Saturn Studio y gestionar tus flujos de trabajo.

*Read this in other languages: [English](Manual_SaturnStudio.md), [Português](Manual_SaturnStudio.pr.md), [Español](Manual_SaturnStudio.es.md)*

![banner](imgs/Banner_SaturnStudio.jpg)
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

### Subir archivo al File Storage

Sube un archivo al File Storage de tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Path hacia el archivo|Ruta del archivo a subir|C:/Users/User/Downloads/file.file|
|Asignar resultado a variable|Nombre de la variable donde se almacenará el resultado|Variable|

### Listar todos los archivos en el File Storage

Retorna una lista con todos los archivos en el File Storage de tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Retorna una lista con todos los archivos en el File Storage de tu cuenta de Saturn Studio|Variable|

### Eliminar un archivo del File Storage

Elimina un archivo del File Storage de tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo|ID del archivo a eliminar en el File Storage de tu cuenta de Saturn Studio|Archivo|
|Asignar resultado a variable|Nombre de la variable donde se almacenará el resultado|Variable|

### Listar todos los robots en Saturn Studio

Retorna una lista con todos los robots de tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Retorna una lista con todos los robots de tu cuenta de Saturn Studio|Variable|
|Filtrar robots activos|Marca para solo listar los robots activos|True|

### Detener todos los robots en ejecución

Detiene todos los robots en ejecución en tu cuenta de Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Variable donde se almacenará el resultado de si se pudieron desactivar los robots|Variable|

### Listar Data Stores

Este comando te permite obtener todos los Data Stores de tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Variable donde se almacenarán los Data Stores de tu cuenta de Saturn Studio|Variable|

### Buscar Data Store

Este comando te permite obtener un Data Store usando su ID o Nombre desde tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato a buscar|Selecciona si deseas buscar el Data Store por su ID o Nombre en tu cuenta de Saturn Studio|ID|
|Nombre o ID del Data Store|Nombre o ID del Data Store a buscar en tu cuenta de Saturn Studio|my_data_store \| ID|
|Asignar resultado a variable|Variable donde se almacenará la información de los registros obtenidos del Data Store en tu cuenta de Saturn Studio|Variable|

### Crear Data Store

Este comando te permite crear un Data Store en tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del Data Store|Nombre que tendrá el Data Store creado en tu cuenta de Saturn Studio|Mi nuevo Data Store|
|Descripción del Data Store (opcional)|Descripción que tendrá el Data Store creado en tu cuenta de Saturn Studio|Descripción del Data Store (opcional)|
|Asignar resultado a variable|Variable donde se almacenará la información del Data Store creado en tu cuenta de Saturn Studio|Variable|

### Agregar registro a Data Store

Este comando te permite agregar un registro a un Data Store en tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del Data Store|ID del Data Store donde se agregará el registro|e88d5dfd3c59f0f5fbb908d0f6aaf7ab|
|Registro a agregar (formato JSON)|Registro que se agregará al Data Store en tu cuenta de Saturn Studio|{
  "nombre": "Juan",
  "edad": 30
}|
|Asignar resultado a variable|Variable donde se almacenará la información del registro agregado al Data Store en tu cuenta de Saturn Studio|Variable|

### Obtener registros de Data Store

Este comando te permite obtener registros de un Data Store en tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del Data Store|ID del Data Store desde donde se obtendrán los registros|e88d5dfd3c59f0f5fbb908d0f6aaf7ab|
|Filtro personalizado|Solo se obtendrán los registros que contengan el texto especificado en el filtro. Deja este campo vacío para obtener todos los registros.|"nombre": "Juan"|
|Asignar resultado a variable|Variable donde se almacenará la información de los registros obtenidos del Data Store en tu cuenta de Saturn Studio|Variable|

### Actualizar registro en Data Store

Este comando te permite actualizar un registro en un Data Store en tu cuenta de Saturn Studio
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del Data Store|ID del Data Store donde se actualizará el registro|e88d5dfd3c59f0f5fbb908d0f6aaf7ab|
|ID del Registro|ID del registro a actualizar en el Data Store|bb24f3e07b147d16ba3ca9b25b181695|
|Nuevos datos (formato JSON)|Nuevos datos que sobrescribirán el registro. El registro será actualizado con los valores proporcionados.|{
  "nombre": "Juan",
  "edad": 31
}|
|Asignar resultado a variable|Variable donde se almacenará la información del registro actualizado en tu cuenta de Saturn Studio|Variable|

### Listar robots compartidos

Retorna una lista con los robots compartidos contigo en Saturn Studio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Variable donde se almacenará el listado de robots compartidos|Variable|

### Ejecutar robot compartido

Ejecuta un robot compartido indicando su Project ID y Robot ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Team ID|ID del equipo que comparte el robot|team_id|
|Robot ID|ID del robot compartido a ejecutar|robot_id|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|Variable|
