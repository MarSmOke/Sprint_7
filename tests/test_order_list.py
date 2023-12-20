import allure
from api_methods.orders import *


class TestOrderList:
    @allure.title("Successful order list retrieval")
    @allure.description("Get an order list with filtration parameters")
    def test_get_order_list(self):
        assert get_order_list().status_code == 200 and get_order_list().json()["orders"]
