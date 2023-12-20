import requests
import data


def courier_login(payload):
    response = requests.post(url=data.main_url+data.login_url, data=payload)
    return response


def login_incorrect_data():
    login = data.generate_random_string(10)
    password = data.generate_random_string(10)

    payload = {
        "login": login,
        "password": password
    }

    response = requests.post(url=data.main_url+data.login_url, data=payload)
    return response
