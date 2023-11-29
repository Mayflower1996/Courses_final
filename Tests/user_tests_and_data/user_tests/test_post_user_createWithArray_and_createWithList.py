import requests
from jsonschema import validate
from user_data.user_create_payload import CORRECT_TWO_USERS_PAYLOAD, INCORRECT_USER_PAYLOAD_NOT_ARRAY, \
    INCORRECT_USER_PAYLOAD_EMPTY_FIELDS, CORRECT_ONE_USER_PAYLOAD
from user_data.url_headers_auth_token import HEADERS
from user_data.user_response_schema import RESPONSE_SCHEMA


def test_response_schema(endpoint_url):
    url = endpoint_url
    response = requests.post(url, headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
    assert response.status_code == 200
    validate(instance=response.json(), schema=RESPONSE_SCHEMA)


def test_create_two_users(endpoint_url):
    url = endpoint_url
    response = requests.post(url, headers=HEADERS, json=CORRECT_TWO_USERS_PAYLOAD)
    assert response.status_code == 200
    assert "ok" in response.text.lower()


def test_create_user_not_array(endpoint_url):
    url = endpoint_url
    response = requests.post(url, headers=HEADERS, json=INCORRECT_USER_PAYLOAD_NOT_ARRAY)
    assert response.status_code == 500
    assert "something bad happened" in response.text


def test_create_user_with_empty_fields(endpoint_url):
    url = endpoint_url
    response = requests.post(url, headers=HEADERS, json=INCORRECT_USER_PAYLOAD_EMPTY_FIELDS)
    assert response.status_code == 500
    assert "something bad happened" in response.text
