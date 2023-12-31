import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.pet_get_schema import PetSchema as ps


def test_get_find_existed_pet_by_id(new_pet_data):
    url = f"{u.URL_PET}/{new_pet_data}"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert "id" in response.json()
        validate(instance=response.json(), schema=ps.PET_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get pet by ID, status code: {response.status_code}")


def test_find_not_existed_pet_by_id(not_existing_pet_id):
    url = f"{u.URL_PET}/{not_existing_pet_id}"
    response = requests.get(url)
    if response.status_code == 404 or "Pet not found" in response.json():
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Pet with ID {not_existing_pet_id} exists, status code: {response.status_code}")
