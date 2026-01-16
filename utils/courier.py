import requests
import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'

def generate_random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []

def create_courier(data):
    response = requests.post(BASE_URL, json=data)
    return response


def delete_courier(courier_id):
    url = f"{BASE_URL}/{courier_id}"
    response = requests.delete(url)
    return response

def login_courier(login_data):
    return requests.post(f"{BASE_URL}/login", json=login_data)