import pytest
import requests
from jsonschema.validators import validate
from data.response_schema import RESPONSE_SCHEMA
from data.url_headers import HEADERS, URL_USER
from data.user_get_schema import USER_GET_VALID_RESPONSE_SCHEMA


def test_get_valid_user(valid_username_create):
    url = f"{URL_USER}/{valid_username_create}"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert "username" in response.json()
        assert "id" in response.json()
        validate(instance=response.json(), schema=USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get user by username, status code: {response.status_code}")


def test_get_invalid_user(invalid_username):
    url = f"{URL_USER}/{invalid_username}"
    response = requests.get(url)
    if response.status_code == 404:
        assert "not found" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Username exists, status code: {response.status_code}")


def test_empty_username():
    url = f"{URL_USER}/"
    response = requests.post(url, headers=HEADERS, json={})
    if response.status_code == 404 or 400:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Empty username exists, status code: {response.status_code}")
