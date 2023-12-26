import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.url_headers import URL as u
from data_for_tests.user_get_schema import UserSchema as us


def test_get_valid_user(valid_username_create):
    url = f"{u.URL_USER}/{valid_username_create}"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert "username" in response.json()
        assert "id" in response.json()
        validate(instance=response.json(), schema=us.USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get user by username, status code: {response.status_code}")


def test_get_invalid_user(invalid_username):
    url = f"{u.URL_USER}/{invalid_username}"
    response = requests.get(url)
    if response.status_code == 404:
        assert "not found" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Username exists, status code: {response.status_code}")


def test_empty_username():
    url = f"{u.URL_USER}/"
    response = requests.post(url, headers=u.HEADERS, json={})
    if response.status_code == 404 or 400:
        assert "200" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Empty username exists, status code: {response.status_code}")
