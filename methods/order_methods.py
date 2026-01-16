import requests
import allure
from data.data import BASE_URL, ORDER_URL

URL = f'{BASE_URL}{ORDER_URL}'

class OrderMethods:

    @allure.step("Создаём заказ с телом: {order_data}")
    def create_order(self, order_data):
        return requests.post(URL, json=order_data)
