import requests
import data
import json


def create_order():
    response = requests.post(data.order_url, data=json.dumps(data.order_data))
    return response


def get_order_list():
    response = requests.get(data.filtered_orders_url)
    return response
