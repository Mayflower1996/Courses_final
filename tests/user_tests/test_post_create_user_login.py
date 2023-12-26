import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.url_headers import URL as u


def test_create_user_login(valid_login_user, user_payload_correct, valid_login):
    if valid_login_user == 200:
        url = f"{u.URL_USER}/"
        response = requests.post(url, headers=u.HEADERS, json=user_payload_correct)
        assert response.status_code == 200
        assert "200" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login failed, status code: {valid_login_user}")


def test_create_user_not_login(user_payload_correct):
    url = f"{u.URL_USER}/"
    response = requests.post(url, headers=u.HEADERS, json=user_payload_correct)
    if response.status_code == 401 or 403:
        assert response.status_code == 401 or 403
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


def test_create_user_invalid_payload_login(valid_login_user, user_payload):
    if valid_login_user == 200:
        url = f"{u.URL_USER}/"
        response = requests.post(url, headers=u.HEADERS, json=user_payload)
        if response.status_code == 500:
            assert "something bad happened" in response.text
            validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
        else:
            pytest.fail(f"User created, status code: {response.status_code}")
    else:
        pytest.fail(f"User login failed, status code: {valid_login_user}")
