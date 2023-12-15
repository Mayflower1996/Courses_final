import pytest
import requests
from jsonschema.validators import validate
from jsonschema import ValidationError
from data.url_headers import URL_PET, HEADERS
from data.response_schema import RESPONSE_SCHEMA
from data.pet_create_payload import UPDATE_PET



def test_update_pet_name(create_and_update_pet):
    response_get = requests.get(f"{URL_PET}/{create_and_update_pet}")
    assert response_get.status_code == 200, f"Failed to get updated pet, status code: {response_get.status_code}"
    response = requests.put(URL_PET, headers=HEADERS, json=UPDATE_PET)
    if response.status_code == 200:
        try:
            validate(instance=response_get.json(), schema=RESPONSE_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")
        assert response_get.json() == UPDATE_PET
    else:
        pytest.fail(f"Pet update failed, status code: {response.status_code}")

