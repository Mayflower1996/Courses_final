import pytest
import requests
from jsonschema import validate
from data.response_schema import RESPONSE_SCHEMA
from data.url_headers import HEADERS, URL_USER


def test_update_user(valid_username_create, user_payload_correct):
    url = f"{URL_USER}/{valid_username_create}"
    response = requests.put(url, headers=HEADERS, json=user_payload_correct)
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User update failed, status code: {response.status_code}")


def test_update_invalid_payload_user(valid_username_create, user_payload):
    url = f"{URL_USER}/{valid_username_create}"
    response = requests.put(url, headers=HEADERS, json=user_payload)
    if response.status_code == 500:
        assert "something bad happened" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User updated, status code: {response.status_code}")
