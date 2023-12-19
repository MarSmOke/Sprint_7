import allure
from api_methods.orders import *


class TestOrderList:
    @allure.title("Get an order list")
    @allure.description("Get an order list")
    def test_get_order_list(self):
        assert get_order_list().status_code == 200 and get_order_list().json()["orders"]
