import requests

class SaturnClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def connect(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        response = requests.post(f"{self.base_url}/user/userInfo", headers=headers)
        
        if response.status_code != 200:
            raise Exception("Failed to connect to Saturn API: " + response.text)
        
        return True

    def execute_flow(self, workflow_url: str):
        
        folder_id = workflow_url.split("d=")[-1].split("&")[0]
        flow_id = workflow_url.split("i=")[-1].split("&")[0]
        
    
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(f"{self.base_url}/execute/{folder_id}/{flow_id}", headers=headers)
        print(response.status_code)
        print(response.text)
        if response.status_code != 200:
            raise Exception("Failed to execute workflow in Saturn: " + response.text)

        return response.json()