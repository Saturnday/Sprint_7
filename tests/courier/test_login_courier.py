import allure
import pytest
from methods.courier_methods import CourierMethods
from data.data import LoginCourier

courier = CourierMethods()

@allure.title("Курьер может авторизоваться с валидными данными")
def test_courier_can_login(new_courier):
    login_data = {
        "login": new_courier["login"],
        "password": new_courier["password"]
    }
    status, body = courier.login_courier(login_data)

    with allure.step("Проверяем, что код ответа 200 и есть id в теле"):
        assert status == 200
        assert "id" in body


@allure.title("Авторизация без обязательных полей должна завершаться ошибкой")
@pytest.mark.parametrize("login_data", LoginCourier.login_with_missing_fields())
def test_login_missing_required_fields(login_data):
    status, body = courier.login_courier(login_data)

    with allure.step("Проверяем, что код 400 и сообщение содержит 'Недостаточно данных'"):
        assert status == 400
        assert "message" in body
        assert "Недостаточно данных" in body["message"]


@allure.title("Авторизация с несуществующим логином/паролем должна завершаться ошибкой")
def test_login_with_wrong_credentials():

    status, body = courier.login_courier(LoginCourier.non_exist_account())

    with allure.step("Проверяем, что код 404 или 400 и есть сообщение об ошибке"):
        assert status in (400, 404)
        assert "message" in body
