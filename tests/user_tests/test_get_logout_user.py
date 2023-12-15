import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.response_schema import RESPONSE_SCHEMA
from data_for_tests.url_headers import URL_USER, HEADERS


def test_logout_user(valid_login_user, valid_login):
    if valid_login_user == 200:
        url = f"{URL_USER}/logout"
        response = requests.get(url, headers=HEADERS, json={})
        assert response.status_code == 200
        assert "ok" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        url = f"{URL_USER}/logout"
        response = requests.get(url, headers=HEADERS, json={})
        assert response.status_code != 200
        assert "error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        pytest.fail(f"User login failed, status code: {valid_login_user}")
