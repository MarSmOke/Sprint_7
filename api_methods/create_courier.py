import requests
import data


def register_new_courier():
    login = data.generate_random_string(10)
    password = data.generate_random_string(10)
    first_name = data.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(data.create_url, data=payload)
    return response


def register_the_same_courier():
    login = data.generate_random_string(10)
    password = data.generate_random_string(10)
    first_name = data.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    requests.post(data.create_url, data=payload)
    response = requests.post(data.create_url, data=payload)
    return response


def register_without_fields(payload):
    response = requests.post(data.create_url, data=payload)
    return response

