import os

class Config:
    BASE_URL=os.getenv("BASSE_URL","http://localhost:8000/")
    API_URL=BASE_URL+"/api/v1"

    USERNAME=os.getenv("TAGCARE_EMAIL","qa.user@tagcare.test")
    PASSWORD = os.getenv("TAGCARE_PASSWORD", "Test@1234")

    USER2_EMAIL="ops.user@tagcare.test"
    USER2_PASSWORD="Test@5678"

    BROWSER=os.getenv("BROWSER","chrome")

