import pytest
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"


def test_courier_can_login(new_courier):
    login_data = {
        "login": new_courier["login"],
        "password": new_courier["password"]
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response, f"Ответ не содержит id: {json_response}"



@pytest.mark.parametrize("login_data", [
    {"login": "", "password": "pass"},
    {"login": "login", "password": ""},
    {"login": "", "password": ""}
])
def test_login_missing_required_fields(login_data):
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 400
    assert "message" in response.json()
    assert "Недостаточно данных" in response.json()["message"]


def test_login_with_wrong_credentials():
    login_data = {
        "login": "nonexistent",
        "password": "wrongpass"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 404 or response.status_code == 400
    assert "message" in response.json()
