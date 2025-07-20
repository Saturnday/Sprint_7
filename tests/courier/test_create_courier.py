import allure
import pytest
from data.data import CreateCourier
from methods.courier_methods import CourierMethods

courier = CourierMethods()

@allure.title("Успешное создание курьера")
def test_create_courier_success():
    courier_data = CreateCourier.get_data()
    status, body = courier.create_courier(courier_data)

    with allure.step("Проверяем, что статус 201 и тело содержит 'ok: true'"):
        assert status == 201, f"Expected 201, got {status}"
        assert body.get("ok") is True


@allure.title("Создание двух одинаковых курьеров должно завершаться ошибкой")
def test_identical_couriers_fails():
    courier_data = CreateCourier.get_data()

    first_status, first_body = courier.create_courier(courier_data)
    assert first_status == 201

    second_status, second_body = courier.create_duplicate_courier(courier_data)

    with allure.step("Проверяем, что второй запрос вернул 409 и сообщение об ошибке"):
        assert second_status == 409
        assert "message" in second_body
        assert "Этот логин уже используется" in second_body["message"]


@allure.title("Создание курьера без обязательного поля должно завершаться ошибкой")
@pytest.mark.parametrize("incomplete_data", CreateCourier.get_incomplete_data())
def test_create_courier_missing_required_field(incomplete_data):
    status, body = courier.create_incomplete_courier(incomplete_data)

    with allure.step("Проверяем, что получен код 400 и сообщение об ошибке"):
        assert status == 400, f"Expected 400, got {status}"
        assert "message" in body


@allure.title("Авторизация с некорректными данными должна завершаться ошибкой")
def test_login_with_wrong_credentials():
    login_data = {
        "login": "nonexistent",
        "password": "wrongpass"
    }
    status, body = courier.login_courier(login_data)

    with allure.step("Проверяем, что получен код 404 или 400 и сообщение об ошибке"):
        assert status in [400, 404], f"Expected 400 or 404, got {status}"
        assert "message" in body
