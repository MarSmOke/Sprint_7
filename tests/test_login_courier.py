import allure
import pytest
import data
from api_methods.login import *


class TestLoginCourier:
    @allure.title("Successful courier login")
    @allure.description("Courier login with existing credentials")
    def test_login_successful(self):
        response = courier_login(data.existing_user)
        assert response.status_code == 200 and response.json()["id"]

    @allure.title("Non-existent courier login")
    @allure.description("Courier login with non-registered credentials, expected error")
    def test_login_no_user_error(self):
        response = courier_login(data.generate_credentials())
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Existent courier login with invalid data")
    @allure.description("Courier login with invalid credentials, expected error")
    @pytest.mark.parametrize('payload', [{
                             "login": "msmirnovates",
                             "password": "1234"}, {
                             "login": "msmirnovatest",
                             "password": "12345"}])
    def test_login_invalid_credentials_error(self, payload):
        response = courier_login(payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Courier login without mandatory fields")
    @allure.description("Courier login without login or password, expected error")
    @pytest.mark.parametrize('payload', [{"password": 'password'}, {"login": 'login'}])
    def test_login_without_required_field_error(self, payload):
        response = courier_login(payload)
        assert (response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа")

