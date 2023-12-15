import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL_PET, HEADERS
from data_for_tests.response_schema import RESPONSE_SCHEMA


def test_delete_pet(new_pet_data):
    url = f"{URL_PET}/{new_pet_data}"
    response = requests.delete(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Pet was not deleted, status code: {response.status_code}")


def test_delete_not_existed_pet(not_existing_pet_id):
    url = f"{URL_PET}/{not_existing_pet_id}"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 404
