import pytest
import requests
from jsonschema.validators import validate
from user_data.url_headers_auth_token import URL, HEADERS
from user_data.user_create_payload import CORRECT_ONE_USER_PAYLOAD, CORRECT_TWO_USERS_PAYLOAD, \
    INCORRECT_USER_PAYLOAD_LARGE_STATUS
from user_data.user_get_schema import RESPONSE_SCHEMA


@pytest.mark.order(11)
def test_create_user_login(good_login_user):
    if good_login_user == 200:
        url = f"{URL}/"
        response = requests.post(url, headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
        assert response.status_code == 200
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User login failed with status code: {good_login_user}")


@pytest.mark.order(12)
def test_create_user_not_login():
    url = f"{URL}/"
    response = requests.post(url, headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
    if response.status_code == 401 or 403:
        assert response.status_code == 401 or 403
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User create success with status code: {response.status_code}")


@pytest.mark.order(13)
def test_create_two_users_and_large_status_and_empty_fields_login(good_login_user, user_payload):
    if good_login_user == 200:
        url = f"{URL}/"
        response = requests.post(url, headers=HEADERS, json=user_payload)
        if response.status_code == 500:
            assert "something bad happened" in response.text
            validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        else:
            pytest.fail(f"User created, status code: {response.status_code}")
    else:
        pytest.fail(f"User login failed with status code: {good_login_user}")
