import requests
from jsonschema import validate
from user_data.user_createWithArray_payload import CORRECT_TWO_USERS_PAYLOAD, INCORRECT_USER_PAYLOAD_NOT_ARRAY, \
    INCORRECT_USER_PAYLOAD_EMPTY_FIELDS, CORRECT_ONE_USER_PAYLOAD
from user_data.url_headers_auth_token import HEADERS, URL
from user_data.user_response_schema import RESPONSE_SCHEMA


def test_response_schema():
    response = requests.post(f"{URL}/createWithArray", headers=HEADERS, json=CORRECT_ONE_USER_PAYLOAD)
    assert response.status_code == 200
    assert "ok" in response.text.lower()
    validate(instance=response.json(), schema=RESPONSE_SCHEMA)


def test_create_two_users():
    response = requests.post(f"{URL}/createWithArray", headers=HEADERS, json=CORRECT_TWO_USERS_PAYLOAD)
    assert response.status_code == 200
    assert "ok" in response.text.lower()


def test_create_user_not_array():
    response = requests.post(f"{URL}/createWithArray", headers=HEADERS, json=INCORRECT_USER_PAYLOAD_NOT_ARRAY)
    assert response.status_code == 500
    assert "something bad happened" in response.text


def test_create_user_with_empty_fields():
    response = requests.post(f"{URL}/createWithArray", headers=HEADERS, json=INCORRECT_USER_PAYLOAD_EMPTY_FIELDS)
    assert response.status_code == 500
    assert "something bad happened" in response.text
