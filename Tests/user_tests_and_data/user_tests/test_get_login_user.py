import pytest
import requests
from jsonschema.validators import validate
from user_data.url_headers_auth_token import URL, HEADERS
from user_data.user_get_schema import RESPONSE_SCHEMA


@pytest.mark.order(9)
def test_good_login_user(good_login):
    url = good_login
    response = requests.get(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "logged in user session" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login failed with status code: {response.status_code}")


@pytest.mark.order(10)
def test_login_bad_user(bad_login):
    url = bad_login
    response = requests.get(url, headers=HEADERS, json={})
    if response.status_code == 400:
        assert "error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login success with status code: {response.status_code}")


@pytest.mark.order(11)
def test_login_bad_pass():
    url = f"{URL}/login?username=testuser1&password=gsdfgsdfg"
    response = requests.get(url, headers=HEADERS, json={})
    if response.status_code == 400:
        assert "error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login success with status code: {response.status_code}")
