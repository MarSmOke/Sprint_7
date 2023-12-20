import pytest
import allure
from api_methods.orders import *


class TestOrder:
    @allure.title("Successful order creation")
    @allure.description("Create order with valid color combinations")
    @pytest.mark.parametrize(
        'colors',
        [
            ["BLACK", "GREY"],
            ["BLACK"],
            ["GREY"],
            []
        ]
    )
    def test_login_successful(self, colors):
        data.order_data["color"] = colors
        print(str(create_order().text))
        print(str(data.order_data))
        assert create_order().status_code == 201 and create_order().json()["track"]
