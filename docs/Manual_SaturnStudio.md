



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
