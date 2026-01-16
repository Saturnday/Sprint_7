import requests
import allure
from data.data import BASE_URL, COURIER_URL

URL = f'{BASE_URL}{COURIER_URL}'

class CourierMethods:

    @allure.step("Создание курьера с данными: {courier_data}")
    def create_courier(self, courier_data):
        response = requests.post(URL, json=courier_data)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step("Повторная попытка создать курьера с теми же данными: {courier_data}")
    def create_duplicate_courier(self, courier_data):
        response = requests.post(URL, json=courier_data)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step("Создание курьера без обязательных полей: {incomplete_data}")
    def create_incomplete_courier(self, incomplete_data):
        response = requests.post(URL, json=incomplete_data)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step("Авторизация с логином: {login_data}")
    def login_courier(self, login_data):
        response = requests.post(f"{URL}/login", json=login_data)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, {"message": response.text} 
    
