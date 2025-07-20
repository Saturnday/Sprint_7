import pytest
import requests
import allure
from utils.order import generate_order_data

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

@pytest.mark.parametrize("colors", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
])
@allure.title("Проверка создания заказа с разными цветами")
def test_create_order_with_colors(colors):
    payload = generate_order_data()
    payload["color"] = colors

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert "track" in response.json()

@allure.step("Создаём заказ с телом: {order_data}")
def create_order(order_data):
    return requests.post(BASE_URL, json=order_data)

@allure.step("Проверяем, что статус код равен 201 и в ответе есть track")
def assert_order_created(response):
    assert response.status_code == 201
    assert "track" in response.json()
