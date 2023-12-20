import random
import string

main_url = 'https://qa-scooter.praktikum-services.ru/'
create_url = 'api/v1/courier'
login_url = 'api/v1/courier/login'
order_url = 'api/v1/orders'
filtered_orders_url = 'api/v1/orders?limit=1&page=0&nearestStation=["1"]'

existing_user = {
    "login": "msmirnovatest",
    "password": "1234"}

order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_credentials():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
