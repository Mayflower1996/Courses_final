import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.response_schema import RESPONSE_SCHEMA
from data_for_tests.url_headers import HEADERS, URL_USER


def test_delete_user(valid_username_create):
    url = f"{URL_USER}/{valid_username_create}"
    response = requests.delete(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User updated, status code: {response.status_code}")


def test_delete_not_found_user(invalid_username):
    url = f"{URL_USER}/{invalid_username}"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 404


def test_delete_empty_user():
    url = f"{URL_USER}/"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 400 or 405
