import pytest
from utils.courier import generate_random_string, create_courier, delete_courier, login_courier

@pytest.fixture
def new_courier():
    data = {
        "login": generate_random_string(8),
        "password": generate_random_string(8),
        "firstName": "TestCourier"
    }
    create_response = create_courier(data)
    assert create_response.status_code == 201, (
        f"Ошибка при создании курьера: {create_response.status_code} - {create_response.text}"
    )

    # Логинимся чтобы получить id курьера
    login_response = login_courier({
        "login": data["login"],
        "password": data["password"]
    })
    assert login_response.status_code == 200, (
        f"Ошибка при логине курьера: {login_response.status_code} - {login_response.text}"
    )
    data["id"] = login_response.json().get("id")

    yield data

    # Удаляем курьера по id
    delete_response = delete_courier(data["id"])
    assert delete_response.status_code == 200, (
        f"Ошибка при удалении курьера: {delete_response.status_code} - {delete_response.text}"
    )
