from api.api_Client import APIClient
from config.config import Config

def test_Valid_login():
    api=APIClient()

    response=api.login(Config.USERNAME,Config.PASSWORD)
    print(response.status_code)
    print(response.json())

    assert response.status_code==200
    assert api.token is not None



