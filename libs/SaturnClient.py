import requests

class SaturnClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def connect(self):
        
        response = self.__request__(method="POST", url_end="/user/userInfo", exception_message="Failed to connect to Saturn API")
        
        return True

    def execute_flow(self, workflow_url: str):
        
        folder_id = workflow_url.split("d=")[-1].split("&")[0]
        flow_id = workflow_url.split("i=")[-1].split("&")[0]
        
        response = self.__request__(method="POST", url_end=f"/execute/{folder_id}/{flow_id}", exception_message="Failed to execute workflow in Saturn")

        return response.json()
    
    def upload_file(self, file, robot_id, db):        

        files = {
            "file": (file, open(file, "rb")),
        }

        data = {
            "robot_id": robot_id,
            "db": db
        }
        
        response = self.__request__(method="POST", url_end="/files/upload", exception_message="Failed to upload file to Saturn", data=data, files=files)

        return response.json()
    
    def list_files(self):        
        
        response =  self.__request__(method="GET", url_end="/files/list", exception_message="Failed to list files in Saturn")

        response_data = response.json().get("data", {})
        file_list = response_data.get("files", [])

        return file_list
    
    def delete_file(self, file_id):        
        
        if not self.__does_file_exists__(file_id):
            raise Exception("File with id " + file_id + " does not exist in Saturn")

        data = {
            "id": file_id
        }

        response = self.__request__(method="POST", url_end="/files/delete", exception_message="Failed to delete file in Saturn", data=data)

        success = response.json().get("success", "false")

        return success
    
    def list_robots(self, only_actives):        
    
        response = self.__request__(method="POST", url_end="/project/list", exception_message="Failed to list robots in Saturn")

        project_list = response.json().get("data", [])
        robot_list = self.__get_robot_list__(project_list)

        if only_actives:
            return list(filter(self.__is_active__, robot_list))

        return robot_list
    
    def stop_all_robots(self):   

        response = self.__request__(method="POST", url_end="/project/list", exception_message="Failed to list robots in Saturn")
        project_list = response.json().get("data", [])

        for project in project_list:
            project_id = project["id"]

            data = {
            "project_id": project_id
            }

            response = self.__request__(method="POST", url_end="/project/get", exception_message="Failed to get robots in Saturn", data=data)

            response_data = response.json().get("data")
            robots = response_data[0].get("bot", [])
            
            self.__stop_project_robots__(project_id, robots)
            
        
        return True
    
    def listDataStores(self):        
        
        response =  self.__request__(method="GET", url_end="/dataStorage/list", exception_message="Failed to get DataStores in Saturn")
        response_data = response.json().get("data", {})
        datastore_list = response_data.get("data", [])
        return datastore_list
    
    def createDataStore(self, name: str, description: str):        
        
        data = {
            "name": name,
            "description": description
        }

        response =  self.__request__(method="POST", url_end="/dataStorage/create", exception_message="Failed to create DataStore in Saturn", data=data)
        
        if not response.json().get("success", False):
            raise Exception(response.json().get("message", "Unknown error"))
        
        response_data = response.json().get("data", {})

        return response_data
    
    def addRecordToDataStore(self, datastore_id: str, record: str):

        try:
            record = eval(record)
            if not isinstance(record, dict) and not isinstance(record, list):
                raise Exception("Record must be a dictionary/list/json object")
        except:
            raise Exception("Record must be a dictionary/list/json object")
        
        response =  self.__request__(method="POST", url_end=f"/dataStorage/add?dataStoreId={datastore_id}", exception_message="Failed to add record to DataStore in Saturn", data=record)
        response_data = response.json().get("data", {})
        
        return response_data
    
    def getRecordsFromDataStore(self, datastore_id: str, custom_filter: str):
        try:
            
            data = {
                "dataStoreId": datastore_id,
                "filter": custom_filter
            }
            
            response =  self.__request__(method="POST", url_end=f"/dataStorage/search", exception_message="Failed to get records from DataStore in Saturn", data=data)
            response_data = response.json().get("data", {})
            
            return response_data
        
        except Exception as e:
            raise Exception("Error getting records from DataStore in Saturn: " + str(e))
    
    def searchDataStore(self, search_type: str, search_value: str):
        try:
            url_end = f"/dataStorage/get"
            
            if search_type == "id":
                url_end += f"?id={search_value}"
            elif search_type == "name":
                url_end += f"?name={search_value}"
            else:
                raise Exception("Invalid search type. Must be 'id' or 'name'")
            
            
            response =  self.__request__(method="GET", url_end=url_end, exception_message="Failed to search DataStore in Saturn")
            response_data = response.json().get("data", {})
            
            return response_data
        
        except Exception as e:
            raise Exception("Error searching DataStore in Saturn: " + str(e))
        
        

    def __request__(self, method, url_end, exception_message, data=None, files=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        if method == "GET":
            response = requests.get(f"{self.base_url}{url_end}", headers=headers)
        
        elif method == "POST":
            response = requests.post(f"{self.base_url}{url_end}", headers=headers, data=data, files=files)

        if response.status_code != 200:
            raise Exception(f"{exception_message}: " + response.text)
        
        return response

    def __does_file_exists__(self, file_id):
        files = self.list_files()

        for file in files:

            if file["id"] == file_id:
                return True
            
        return False

    def __get_robot_list__(self, project_list):

        robot_list = []

        for project in project_list:
            data = {
            "project_id": project["id"]
            }

            response = self.__request__("POST", "/project/get", "Failed to get project robots in Saturn", data=data)

            response_data = response.json().get("data")
            robots = response_data[0].get("bot", [])
            robot_list.extend(robots)

        return robot_list
    
    def __is_active__(self, robot):
        return robot.get("status") == 1
    
    def __stop_project_robots__(self, project_id, robots):
        for robot in robots:
            if self.__is_running__(robot):
                data = {
                        "bot_id": robot.get("id"),
                        "project_id": project_id
                    }

                response = self.__request__("POST", "/robot/stop", "Failed to stop all active robots", data=data)

    def __is_running__(self, robot):
        return robot.get("running") == True
    
