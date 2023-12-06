import pytest
import requests
from jsonschema.validators import validate
from Tests.pet_tests_and_data.pet_data.url_headers import URL, HEADERS
# from pet_get_schema import PET_GET_VALID_RESPONSE_SCHEMA
from Tests.pet_tests_and_data.pet_data.url_headers import CORRECT_ONE_PET_PAYLOAD


def test_find_pet_by_id(new_pet_data):
    assert new_pet_data is not None  # Ensure that the fixture returned data

    pet_id = new_pet_data[0]['id']
    response = requests.get(f"{URL}/{pet_id}", headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    assert response.json()["name"] == CORRECT_ONE_PET_PAYLOAD["name"]
    assert response.json()["status"] == CORRECT_ONE_PET_PAYLOAD["status"]
    # Add more assertions as needed based on your specific response structure
