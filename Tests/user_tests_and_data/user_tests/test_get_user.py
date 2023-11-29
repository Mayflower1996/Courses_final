import requests
from jsonschema.validators import validate
from user_data.url_headers_auth_token import HEADERS, URL
from user_data.user_get_schema import USER_GET_OK_RESPONSE_SCHEMA, USER_GET_BAD_RESPONSE_SCHEMA


def test_get_good_user(good_username):
    username = good_username
    url = f"{URL}/{username}"
    response = requests.get(url)
    assert response.status_code == 200
    assert "username" in response.json()
    assert "id" in response.json()
    validate(instance=response.json(), schema=USER_GET_OK_RESPONSE_SCHEMA)


def test_get_bad_user(bad_username):
    username = bad_username
    url = f"{URL}/{username}"
    response = requests.get(url)
    assert response.status_code == 404
    assert "User not found" in response.text
    validate(instance=response.json(), schema=USER_GET_BAD_RESPONSE_SCHEMA)


def test_empty_username():
    url = f"{URL}/"
    response = requests.post(url, headers=HEADERS, json={})
    assert response.status_code == 405
    assert "unknown" in response.text
