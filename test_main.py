from fastapi import FastAPI
from fastapi.testclient import TestClient

## this app is from main.py when we have defined app = FastAPI()
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wiki API call. Call /search or /wiki"}


# test case for phrase
def test_read_phrases():
    response = client.get("phrases/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "res": [
            "barack hussein obama ii",
            "august",
            "american politician",
            "44th president",
        ]
    }
