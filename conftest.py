import pytest

from selenium import webdriver
from config.config import  Config

from api.api_Client import APIClient

@pytest.fixture
def api_client():
    api=APIClient()
    response=api.login(Config.USERNAME,Config.PASSWORD)
    assert response.status_code==200,"Login failed"
    yield api


@pytest.fixture
def browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

