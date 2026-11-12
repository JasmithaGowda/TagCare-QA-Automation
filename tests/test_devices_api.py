from idlelib.rpc import response_queue

from api.api_Client import APIClient
from config.config import Config
from conftest import api_client


# def test_get_device(api_client):
#     api=APIClient()
#     #
#     # # login
#     login_response=api.login(Config.USERNAME,Config.PASSWORD)
#     assert login_response.status_code==200
#
#     #get device
#     response=api_client.get_devices()
#     print(response.status_code)
#     print(response.json())
#
#     assert response.status_code==200

#B1-GET ALL DEVICE
def test_get_devices(api_client):

    #get device
    response=api_client.get_devices()
    assert response.status_code == 200
    data=response.json()
    assert "data" in response.json()
    assert "pagination" in data
    print(data)

def test_device_pagination(api_client):

    login_response=api_client.login(Config.USERNAME,Config.PASSWORD)
    assert login_response.status_code==200
    response_page1=api_client.get_devices(page=1,limit=10)
    response_page2 = api_client.get_devices(page=2, limit=10)

    assert response_page1.status_code==200
    assert response_page2.status_code == 200

    page1_data=response_page1.json()
    page2_data = response_page2.json()

    devices_page1=page1_data["data"]
    devices_page2 = page2_data["data"]


    assert len(devices_page1) <=10
    assert len(devices_page2) <= 10

    ids_page1=[device["device_id"] for device in devices_page1]
    ids_page2 = [device["device_id"] for device in devices_page2]


    print("page 1 ids:",ids_page1)
    print("page 2 ids:", ids_page2)

    assert set(ids_page1).isdisjoint(set(ids_page2)), \
        f"Duplicate device fount:{set(ids_page1).intersection(set(ids_page2))}"



def test_filter_devices_by_status(api_client):
    response=api_client.get_devices(status="ONLINE")
    assert response.status_code==200
    devices=response.json()["data"]
    for device in devices:
        for device in devices:
            assert device["status"]=="ONLINE"



