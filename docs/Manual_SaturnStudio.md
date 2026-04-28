



# Saturn Studio
  
This module allows you to connect to your Saturn Studio account and manage your workflows.  

*Read this in other languages: [English](Manual_SaturnStudio.md), [Português](Manual_SaturnStudio.pr.md), [Español](Manual_SaturnStudio.es.md)*
  
![banner](imgs/Banner_SaturnStudio.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect
  
Connect your account of Saturn Studio using your API Key.
|Parameters|Description|example|
| --- | --- | --- |
|API Key|API Key for Saturn Studio|eyJhbGciOi...|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Execute workflow
  
Execute a workflow from your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|Workflow URL|Workflow URL for Saturn Studio|https://studio.rocketbot.com/flow?d=xxxx&i=yyyy&r=e|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Upload file to File Storage
  
Upload a file to the File Storage of your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|File Path|Path of the file to upload|C:/Users/User/Downloads/file.file|
|Assign result to variable|Name of the variable where the result will be stored|Variable|

### List all files in File Storage
  
Return a list of all files from the File Storage of your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Return a list of all files from the File Storage of your Saturn Studio account|Variable|

### Delete a file from File Storage
  
Delete a file from the File Storage of your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|File ID|ID of the file to delete from the File Storage of your Saturn Studio account|File|
|Assign result to variable|Name of the variable where the result will be stored|Variable|

### List all robots in Saturn Studio
  
Return a list of all robots of your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Return a list of all robots of your Saturn Studio account|Variable|
|Filter active robots|Check to list only active robots|True|

### Stop all running robots
  
Stops all running robots in your Saturn Studio account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Variable where the result of whether the robots could be deactivated will be stored|Variable|

### List Data Stores
  
This command allows you to retrieve all Data Stores from your Saturn Studio account
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Variable where the Data Stores of your Saturn Studio account will be stored|Variable|

### Search Data Store
  
This command allows you to retrieve a Data Store using its ID or Name from your Saturn Studio account
|Parameters|Description|example|
| --- | --- | --- |
|Type of data to search|Select whether you want to search the Data Store by its ID or Name in your Saturn Studio account|ID|
|Data Store Name or ID|Name or ID of the Data Store to search in your Saturn Studio account|my_data_store | ID|
|Assign result to variable|Variable where the retrieved records information from the Data Store in your Saturn Studio account will be stored|Variable|

### Create data store
  
This command allows you to create a Data Store in your Saturn Studio account
|Parameters|Description|example|
| --- | --- | --- |
|Data Store name|Name that the Data Store created in your Saturn Studio account will have|My new Data Store|
|Data Store description (optional)|Description that the Data Store created in your Saturn Studio account will have|Data Store description (optional)|
|Assign result to variable|Variable where the created Data Store information in your Saturn Studio account will be stored|Variable|

### Add record to Data Store
  
This command allows you to add a record to a Data Store in your Saturn Studio account
|Parameters|Description|example|
| --- | --- | --- |
|Data Store ID|ID of the Data Store where the record will be added in your Saturn Studio account|e88d5dfd3c59f0f5fbb908d0f6aaf7ab|
|Record to add (JSON format)|Record that will be added to the Data Store in your Saturn Studio account|{
  "name": "John",
  "age": 30
}|
|Assign result to variable|Variable where the added record information in your Saturn Studio account will be stored|Variable|

### Get records from Data Store
  
This command allows you to get records from a Data Store in your Saturn Studio account
|Parameters|Description|example|
| --- | --- | --- |
|Data Store ID|ID of the Data Store from where the records will be retrieved in your Saturn Studio account|e88d5dfd3c59f0f5fbb908d0f6aaf7ab|
|Custom Filter|Only records containing the specified text in the filter will be retrieved. Leave this field empty to get all records.|"name": "John"|
|Assign result to variable|Variable where the retrieved records information from the Data Store in your Saturn Studio account will be stored|Variable|

### List shared robots
  
Return a list of robots shared with you in Saturn Studio.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Variable where the shared robots list will be stored|Variable|

### Execute shared robot
  
Execute a shared robot by project ID and robot ID.
|Parameters|Description|example|
| --- | --- | --- |
|Project ID|Project ID that owns the shared robot|team_id|
|Robot ID|Shared robot ID to execute|robot_id|
|Assign result to variable|Variable where the execution result will be stored|Variable|
