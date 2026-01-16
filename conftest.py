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
    data["id"] = None

    if create_response.status_code == 201:
        login_response = login_courier({
            "login": data["login"],
            "password": data["password"]
        })
        if login_response.status_code == 200:
            data["id"] = login_response.json().get("id")

    yield data

    if data["id"]:
        delete_courier(data["id"])
