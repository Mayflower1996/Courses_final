import pytest
import requests
from jsonschema.validators import validate
from pet_data.url_headers import URL, HEADERS
from pet_data.pet_get_schema import RESPONSE_SCHEMA

def test_delete_pet(valid_username_create):
    url = f"{URL}/{valid_username_create}"
    response = requests.delete(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"User updated, status code: {response.status_code}")