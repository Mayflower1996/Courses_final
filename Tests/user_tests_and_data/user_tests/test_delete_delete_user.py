import pytest
import requests
from jsonschema.validators import validate
from Tests.user_tests_and_data.user_data.url_headers import HEADERS, URL_USER
from Tests.user_tests_and_data.user_data.user_get_schema import RESPONSE_SCHEMA
from conftest import valid_username_create, invalid_username


@pytest.mark.order(16)
def test_delete_user(valid_username_create):
    url = f"{URL_USER}/{valid_username_create}"
    response = requests.delete(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User updated, status code: {response.status_code}")


@pytest.mark.order(17)
def test_delete_not_found_user(invalid_username):
    url = f"{URL_USER}/{invalid_username}"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 404


@pytest.mark.order(18)
def test_delete_empty_user():
    url = f"{URL_USER}/"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 400 or 405
