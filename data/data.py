from utils.courier import generate_random_string

class CreateCourier:
    @staticmethod
    def get_incomplete_data():
        
        return [
            {
                "login": None,
                "password": generate_random_string(8),
                "firstName": generate_random_string(8)
            },
            {
                "login": generate_random_string(8),
                "password": None,
                "firstName": generate_random_string(8)
            },
            {
                "login": generate_random_string(8),
                "password": generate_random_string(8),
                "firstName": None
            }
        ]
