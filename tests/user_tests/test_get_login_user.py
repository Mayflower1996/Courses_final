import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.url_headers import URL as u


def test_valid_login_user(valid_login):
    url = valid_login
    response = requests.get(url, headers=u.HEADERS, json={})
    if response.status_code == 200:
        assert "logged in user session" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login failed, status code: {response.status_code}")


def test_login_invalid_user(invalid_login):
    url = invalid_login
    response = requests.get(url, headers=u.HEADERS, json={})
    if response.status_code == 400:
        assert "error" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login success, status code: {response.status_code}")


def test_login_invalid_pass():
    url = f"{u.URL_USER}/login?username=testuser1&password=gsdfgsdfg"
    response = requests.get(url, headers=u.HEADERS, json={})
    if response.status_code == 400:
        assert "error" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login success, status code: {response.status_code}")
