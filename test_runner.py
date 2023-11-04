# from Tests import test_root
# import pytest
from fastapi.testclient import TestClient
from FastAPI import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is working"}


if __name__ == '__main__':
    test_root()
