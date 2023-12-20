import allure
import pytest
import data
from api_methods.create_courier import *


class TestCreateCourier:
    @allure.title("Successful courier registration")
    @allure.description("Courier registration with valid data")
    def test_create_courier_successful(self):
        response = register_courier(data.generate_credentials())
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Courier re-registration")
    @allure.description("Courier registration with existing data, expected error")
    def test_create_courier_duplication_error(self):
        response = register_courier(data.existing_user)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Courier registration without one of mandatory fields")
    @allure.description("Courier registration without login or password, expected error")
    @pytest.mark.parametrize('payload', [{"password": 'password'}, {"login": 'login'}])
    def test_create_courier_without_required_field_error(self, payload):
        response = register_courier(payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"