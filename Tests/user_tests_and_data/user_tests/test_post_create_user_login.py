import pytest
import requests
from jsonschema.validators import validate
from Tests.user_tests_and_data.user_data.url_headers import URL, HEADERS
from Tests.user_tests_and_data.user_data.user_get_schema import RESPONSE_SCHEMA
from Tests.conftest import valid_login_user, user_payload_correct, user_payload, valid_login


@pytest.mark.order(12)
def test_create_user_login(valid_login_user, user_payload_correct, valid_login):
    if valid_login_user == 200:
        url = f"{URL}/"
        response = requests.post(url, headers=HEADERS, json=user_payload_correct)
        assert response.status_code == 200
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login failed, status code: {valid_login_user}")


@pytest.mark.order(13)
def test_create_user_not_login(user_payload_correct):
    url = f"{URL}/"
    response = requests.post(url, headers=HEADERS, json=user_payload_correct)
    if response.status_code == 401 or 403:
        assert response.status_code == 401 or 403
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


@pytest.mark.order(14)
def test_create_user_invalid_payload_login(valid_login_user, user_payload):
    if valid_login_user == 200:
        url = f"{URL}/"
        response = requests.post(url, headers=HEADERS, json=user_payload)
        if response.status_code == 500:
            assert "something bad happened" in response.text
            validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        else:
            pytest.fail(f"User created, status code: {response.status_code}")
    else:
        pytest.fail(f"User login failed, status code: {valid_login_user}")
