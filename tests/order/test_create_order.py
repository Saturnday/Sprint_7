import allure
import pytest
from utils.order import generate_order_data
from data.data import OrderData
from methods.order_methods import OrderMethods

order = OrderMethods()

@allure.title("Проверка создания заказа с разными цветами")
@pytest.mark.parametrize("colors", OrderData.create_order_colors)
def test_create_order_with_colors(colors):
    payload = generate_order_data()
    payload["color"] = colors

    response = order.create_order(payload)
    order.assert_order_created(response)
