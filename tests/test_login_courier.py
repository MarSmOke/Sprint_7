import allure
import pytest
from api_methods.login import *


class TestLoginCourier:
    @allure.title("Login with correct data")
    @allure.description("Successful courier login")
    def test_login_successful(self):
        assert courier_login().status_code == 200 and courier_login().json()["id"]

    @allure.title("Login with incorrect data")
    @allure.description("Login with invalid parameters")
    def test_login_no_user_error(self):
        assert (login_incorrect_data().status_code == 404 and
                login_incorrect_data().json()["message"] == "Учетная запись не найдена")

    @allure.title("Login without mandatory fields")
    @allure.description("Login without mandatory fields")
    @pytest.mark.parametrize('payload', [
        {"password": 'password'},
        {"login": 'login'}])
    def test_login_without_required_field_error(self, payload):
        assert (login_without_fields(payload).status_code == 400 and
                login_without_fields(payload).json()["message"] == "Недостаточно данных для входа")

