from datetime import datetime, timedelta

def generate_order_data():
    return {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 911 911 91 91",
        "rentTime": 5,
        "deliveryDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "comment": "Saske, come back to Konoha"
    }