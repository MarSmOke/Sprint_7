import requests
import data


def courier_login():
    response = requests.post(data.login_url, data=data.existing_user)
    return response


def login_without_fields(payload):
    response = requests.post(data.login_url, data=payload)
    return response


def login_incorrect_data():
    login = data.generate_random_string(10)
    password = data.generate_random_string(10)

    payload = {
        "login": login,
        "password": password
    }

    response = requests.post(data.login_url, data=payload)
    return response
