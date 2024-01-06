API tests for the Yandex.Scooter service\

**Repository structure**:
- **api_methods**: contains methods for working with the API;
- **tests**: contains tests covering the specified endpoints of the API;
- **allure_results**: contains the results of running tests;
- **data.py**: contains constants (URLs, profile data, order data) for tests;
- **requirements.txt**: contains information about packages to configure the environment for a successful launch.\

Implemented tests:
- test_create_courier - tests for creating a courier;
- test_create_order - tests for creating an order;
- test_login_courier - tests for courier login;
- test_order_list - test for getting a list of orders.

Command to run: python -m pytest tests \
Command to read results: allure serve allure_results

! Known bugs:
- login attempt with only one login parameter returns 504 (failure due to timeout);
- 404 error for a login attempt by a non-existent user and for a login attempt with typos in the login/password.
