import allure
import pytest
from api_methods.create_courier import *


class TestCreateCourier:
    @allure.title("Registration with correct data")
    @allure.description("Successful registration check")
    def test_create_courier_successful(self):
        assert register_new_courier().status_code == 201 and register_new_courier().json()["ok"]

    @allure.title("Registration with existing data")
    @allure.description("Courier duplication")
    def test_create_courier_duplication_error(self):
        assert (register_the_same_courier().status_code == 409 and
                register_the_same_courier().json()["message"] == "Этот логин уже используется. Попробуйте другой.")

    @allure.title("Registration without mandatory fields")
    @allure.description("Registration without mandatory fields")
    @pytest.mark.parametrize('payload', [
        {"password": 'password',
         "firstName": 'first_name'},
        {"login": 'login',
         "firstName": 'first_name'}])
    def test_create_courier_without_required_field_error(self, payload):
        assert (register_without_fields(payload).status_code == 400 and
                register_without_fields(payload).json()["message"] == "Недостаточно данных для создания учетной записи")