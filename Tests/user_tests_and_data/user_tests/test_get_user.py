import pytest
import requests
from jsonschema.validators import validate
from Tests.user_tests_and_data.user_data.url_headers import HEADERS, URL
from Tests.user_tests_and_data.user_data.user_get_schema import RESPONSE_SCHEMA, USER_GET_VALID_RESPONSE_SCHEMA
from Tests.conftest import valid_username_create, invalid_username # noqa


@pytest.mark.order(6)
def test_get_valid_user(valid_username_create):
    url = f"{URL}/{valid_username_create}"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert "username" in response.json()
        assert "id" in response.json()
        validate(instance=response.json(), schema=USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get user by username, status code: {response.status_code}")


@pytest.mark.order(7)
def test_get_invalid_user(invalid_username):
    url = f"{URL}/{invalid_username}"
    response = requests.get(url)
    if response.status_code == 404:
        assert "User not found" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Username exists, status code: {response.status_code}")


@pytest.mark.order(8)
def test_empty_username():
    url = f"{URL}/"
    response = requests.post(url, headers=HEADERS, json={})
    if response.status_code == 405 or 400:
        assert "unknown" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Empty username exists, status code: {response.status_code}")
