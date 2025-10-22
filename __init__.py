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

except Exception as e:
    PrintException() # type: ignore
    raise e