import requests
import allure
import pytest
from utils.courier import generate_random_string
from data.data import CreateCourier

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

@allure.title("Успешное создание курьера")
def test_create_courier_success():
    payload = {
        "login": generate_random_string(8),
        "password": generate_random_string(8),
        "firstName": generate_random_string(8)
    }
    response = requests.post(BASE_URL, data=payload)
    assert response.status_code == 201
    assert response.json().get("ok") is True

@allure.title("Создание двух одинаковых курьеров должно завершаться ошибкой")
def test_identical_couriers_fails():
    payload = {
        "login": generate_random_string(8),
        "password": generate_random_string(8),
        "firstName": generate_random_string(8)
    }
    first_response = requests.post(BASE_URL, data=payload)
    assert first_response.status_code == 201

    second_response = requests.post(BASE_URL, data=payload)
    assert second_response.status_code == 409
    assert "message" in second_response.json()
    assert "Этот логин уже используется" in second_response.json()["message"]


@allure.title("Создание курьера без обязательного поля должно завершаться ошибкой")
@pytest.mark.parametrize('incomplete_data', CreateCourier.get_incomplete_data())
def test_create_courier_missing_required_field(incomplete_data):
    with allure.step(f"Отправляем запрос с неполными данными: {incomplete_data}"):
        response = requests.post(BASE_URL, json=incomplete_data)

    with allure.step("Проверяем, что получен код 400 и сообщение об ошибке"):
        assert response.status_code == 400, (
            f"Ожидался код 400 при отсутствии обязательного поля. "
            f"Отправленные данные: {incomplete_data}. "
            f"Ответ сервера: {response.text}"
        )
        assert "message" in response.json()

@allure.title("Авторизация с некорректными данными должна завершаться ошибкой")
def test_login_with_wrong_credentials():
    login_data = {
        "login": "nonexistent",
        "password": "wrongpass"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 404 or response.status_code == 400
    assert "message" in response.json()