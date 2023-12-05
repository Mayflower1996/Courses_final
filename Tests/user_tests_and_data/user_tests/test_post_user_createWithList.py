import pytest
import requests
from jsonschema import validate
from Tests.user_tests_and_data.user_data.user_create_payload import CORRECT_TWO_USERS_PAYLOAD, \
    CORRECT_ONE_USER_PAYLOAD, INCORRECT_USER_PAYLOAD_LARGE_STATUS, USER_PAYLOAD_EMPTY_FIELDS
from Tests.user_tests_and_data.user_data.url_headers import HEADERS, URL_USER
from Tests.user_tests_and_data.user_data.user_get_schema import USER_GET_VALID_RESPONSE_SCHEMA, RESPONSE_SCHEMA_ERROR

url = f"{URL_USER}/createWithList"


@pytest.mark.order(1)
def test_response_schema():
    response = requests.post(url, headers=HEADERS, json=[CORRECT_ONE_USER_PAYLOAD])
    if response.status_code == 200:
        validate(instance=response.json(), schema=USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Failed to validate json-schema, status code: {response.status_code}")


@pytest.mark.order(2)
def test_create_two_users():
    response = requests.post(url, headers=HEADERS, json=CORRECT_TWO_USERS_PAYLOAD)
    if response.status_code == 200:
        assert "testuser1" and "testuser2" in response.text.lower()
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")


@pytest.mark.order(3)
def test_create_user_not_array():
    response = requests.post(url, headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
    if response.status_code == 400:
        assert "Input error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA_ERROR)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


@pytest.mark.order(4)
def test_create_user_with_large_status():
    response = requests.post(url, headers=HEADERS, json=[INCORRECT_USER_PAYLOAD_LARGE_STATUS])
    if response.status_code == 400:
        assert "Input error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA_ERROR)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


@pytest.mark.order(5)
def test_create_user_with_empty_fields():
    response = requests.post(url, headers=HEADERS, json=[USER_PAYLOAD_EMPTY_FIELDS])
    if response.status_code == 200:
        assert "username" in response.text
        validate(instance=response.json(), schema=USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")
