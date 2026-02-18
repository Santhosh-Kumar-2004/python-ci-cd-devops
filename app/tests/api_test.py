from fastapi.testclient import TestClient
from app.main import app
import math

client = TestClient(app)


def test_register_success():
    response = client.post("/register", json={
        "email": "test@gmail.com",
        "password": "1234"
    })
    assert response.status_code == 200


def test_register_duplicate():
    client.post("/register", json={
        "email": "dup@gmail.com",
        "password": "1234"
    })

    response = client.post("/register", json={
        "email": "dup@gmail.com",
        "password": "1234"
    })

    assert response.status_code == 400


def test_login_success():
    client.post("/register", json={
        "email": "login@gmail.com",
        "password": "1234"
    })

    response = client.post("/login", json={
        "email": "login@gmail.com",
        "password": "1234"
    })

    assert response.status_code == 200


def test_login_wrong_password():
    client.post("/register", json={
        "email": "wrong@gmail.com",
        "password": "1234"
    })

    response = client.post("/login", json={
        "email": "wrong@gmail.com",
        "password": "9999"
    })

    assert response.status_code == 401
