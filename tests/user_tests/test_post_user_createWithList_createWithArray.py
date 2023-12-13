import pytest
import requests
from jsonschema import validate
from data_for_tests.response_schema import RESPONSE_SCHEMA
from data_for_tests.user_create_payload import CORRECT_TWO_USERS_PAYLOAD, \
    CORRECT_ONE_USER_PAYLOAD, INCORRECT_USER_PAYLOAD_LARGE_STATUS, USER_PAYLOAD_EMPTY_FIELDS
from data_for_tests.url_headers import HEADERS
from data_for_tests.user_get_schema import USER_GET_VALID_RESPONSE_SCHEMA


def test_response_schema(endpoint_url):
    response = requests.post(endpoint_url, headers=HEADERS, json=[CORRECT_ONE_USER_PAYLOAD])
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Failed to validate json-schema, status code: {response.status_code}")


def test_create_two_users(endpoint_url):
    response = requests.post(endpoint_url, headers=HEADERS, json=CORRECT_TWO_USERS_PAYLOAD)
    if response.status_code == 200:
        assert "ok" in response.text.lower()
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")


def test_create_user_not_array(endpoint_url):
    response = requests.post(endpoint_url, headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
    if response.status_code == 500:
        assert "something bad happened" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


def test_create_user_with_large_status(endpoint_url):
    response = requests.post(endpoint_url, headers=HEADERS, json=[INCORRECT_USER_PAYLOAD_LARGE_STATUS])
    if response.status_code == 500:
        assert "something bad happened" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User created, status code: {response.status_code}")


def test_create_user_with_empty_fields(endpoint_url):
    response = requests.post(endpoint_url, headers=HEADERS, json=[USER_PAYLOAD_EMPTY_FIELDS])
    if response.status_code == 200:
        assert "message" in response.text
        validate(instance=response.json(), schema=USER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")
