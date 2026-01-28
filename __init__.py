# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'SaturnStudio' + os.sep + 'libs' + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

from SaturnClient import SaturnClient

global mod_SaturnClient

GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore



module = GetParams("module") # type: ignore

try:
    if module == "connect":
        apikey = GetParams("apikey")
        result = GetParams("result")
        
        try:
            mod_SaturnClient = SaturnClient(
                api_key=apikey,
                base_url="https://studio.rocketbot.com/api"
            )
        
            SetVar(result, mod_SaturnClient.connect())
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error connecting to Saturn: " + str(e))
        

    if module == "execute_flow":
        workflow_url = GetParams("workflow_url")
        result = GetParams("result")
        
        folder_id = workflow_url.split("d=")[-1].split("&")[0]
        flow_id = workflow_url.split("i=")[-1].split("&")[0]
        
        try:
            SetVar(result, mod_SaturnClient.execute_flow(workflow_url))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error executing flow in Saturn: " + str(e))


    if module == "upload_file":
        file = GetParams("file")
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.upload_file(file, robot_id="0", db="0")) #robot_id y db tienen que ser 0
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error uploading file to Saturn: " + str(e))


    if module == "list_files":
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.list_files())
        except Exception as e:
            raise Exception("Error listing files in Saturn: " + str(e))
        

    if module == "delete_file":
        file_id = GetParams("file_id")
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.delete_file(file_id))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error deleting file in Saturn: " + str(e))
        

    if module == "list_robots":
        result = GetParams("result")
        actives = GetParams("actives")

        if actives is not None:
            actives = eval(actives)

        try:
            SetVar(result, mod_SaturnClient.list_robots(actives))
        except Exception as e:
            raise Exception("Error listing robots in Saturn: " + str(e))
        
        
    if module == "stop_all_robots":
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.stop_all_robots())
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error stopping all active robots in Saturn: " + str(e))

    if module == "listDataStores":
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.listDataStores())
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error getting DataStore from Saturn: " + str(e))
          
    if module == "createDataStore":
        name = GetParams("name")
        description = GetParams("description")
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.createDataStore(name, description))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error creating DataStore in Saturn: " + str(e))
        
    if module == "addRecordToDataStore":
        data_store_id = GetParams("data_store_id")
        record = GetParams("record")
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.addRecordToDataStore(data_store_id, record))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error adding record to DataStore in Saturn: " + str(e))
        
    if module == "getRecordsFromDataStore":
        data_store_id = GetParams("data_store_id")
        custom_filter = GetParams("custom_filter")
        result = GetParams("result")

        try:
            SetVar(result, mod_SaturnClient.getRecordsFromDataStore(data_store_id, custom_filter))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error getting records from DataStore in Saturn: " + str(e))
          
    if module == "searchDataStore":
        search_type = GetParams("search_type")
        search_value = GetParams("search_value")
        result = GetParams("result")
        
        try:
            SetVar(result, mod_SaturnClient.searchDataStore(search_type, search_value))
        except Exception as e:
            SetVar(result, False)
            raise Exception("Error searching DataStore in Saturn: " + str(e))

        
except Exception as e:
    PrintException() # type: ignore
    raise e