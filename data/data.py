from utils.courier import generate_random_string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'courier/'
ORDER_URL = 'orders/'

EXPECTED_DUPLICATE_LOGIN_ERROR = "Этот логин уже используется"
EXPECTED_MISSING_FIELD_ERROR = "Недостаточно данных для создания учетной записи"

class CreateCourier:

    @staticmethod
    def get_data():

        return {
            "login": generate_random_string(8),
            "password": generate_random_string(8),
            "firstName": generate_random_string(8)
            }


    @staticmethod
    def get_incomplete_data():
        
        return [
            {
                "password": generate_random_string(8),
                "firstName": generate_random_string(8)
            },
            {
                "login": generate_random_string(8),
                "firstName": generate_random_string(8)
            },
            {
                "login": generate_random_string(8),
                "password": generate_random_string(8),
            }
        ]
class LoginCourier:
    @staticmethod
    def login_with_missing_fields():
        return [
            {"login": "", "password": "pass"},
            {"login": "login", "password": ""},
            {"login": "", "password": ""}
            ]
    @staticmethod
    def non_exist_account():
        return {
        "login": "nonexistent",
        "password": "wrongpass"
        }
    
class OrderData:
    create_order_colors = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]


