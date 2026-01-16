import allure
import pytest
from utils.order import generate_order_data
from data.data import OrderData
from methods.order_methods import OrderMethods

order = OrderMethods()

class TestCreateOrder:

    @allure.title("Проверка создания заказа с разными цветами")
    @pytest.mark.parametrize("colors", OrderData.create_order_colors)
    def test_create_order_with_colors(self, colors):
        payload = generate_order_data()
        payload["color"] = colors

    def test_order_created(self):
        payload = generate_order_data()
        response = order.create_order(payload)
        response_json = response.json()
        assert response.status_code == 201 and isinstance(response_json.get("track"), int)
