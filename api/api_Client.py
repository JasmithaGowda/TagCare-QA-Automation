import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url=Config.API_URL
        self.session=requests.Session()
        self.token=None


    def login(self,email,password):
        url=self.base_url+"/login"
        payload={
            "email":email,
            "password":password
        }

        response=self.session.post(url,json=payload)

        if response.status_code==200:
            self.token=response.json()["token"]

        return response

    def get_headers(self):
        return {
            "Authorization":f"Bearer {self.token}"
        }


    def get_devices(self,page=1,limit=10,status=None):
        url=self.base_url+"/devices"

        params={
            "page":page,
            "limit":limit
        }

        if status:
            params["status"]=status

        response= self.session.get(url,headers=self.get_headers(),params=params)
        print("requests url:",response.url)
        return response


    #get particular device
    def get_device(self,device_id,new_name):
        url=self.base_url+f"/devices/{device_id}"

        return self.session.get(url, headers=self.get_headers())

    #rename a device

    def rename_device(self,device_id,new_name):
        url=self.base_url+f"/devices/{device_id}"

        payload={
            "name":new_name
        }

        return self.session.patch(url,json=payload,headers=self.get_headers())





