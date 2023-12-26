import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs
from jsonschema import ValidationError
from data_for_tests.pet_get_schema import PetSchema as ps


def test_find_pet_by_valid_status(pet_statuses):
    for status in pet_statuses:
        url = f"{u.URL_PET}/findByStatus?status={status}"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to get pets by status '{status}', " \
                                            f"status code: {response.status_code}"
        pets = response.json()
        pet_count = len(pets)
        print(f"Number of pets with status '{status}': {pet_count}")
        try:
            for pet in response.json():
                validate(instance=pet, schema=ps.PET_GET_VALID_RESPONSE_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")


def test_find_pets_with_invalid_status(invalid_pet_status):
    url = f"{u.URL_PET}/findByStatus?status={invalid_pet_status}"
    response = requests.get(url)
    if response.status_code == 400 or "Invalid status value" in response.json():
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Pet with incorrect status {invalid_pet_status} can be found, status code: {response.status_code}")


def test_find_pets_with_empty_status(empty_pet_status):
    url = f"{u.URL_PET}/findByStatus?status={empty_pet_status}"
    response = requests.get(url)
    if response.status_code == 400 or "Invalid status value" in response.json():
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Pet with empty status can be found, status code: {response.status_code}")
