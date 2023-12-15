import pytest
import requests
from jsonschema.validators import validate
from jsonschema import ValidationError
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.pet_create_payload import PetPayload as pp


def test_update_pet_name(create_and_update_pet):
    response_get = requests.get(f"{u.URL_PET}/{create_and_update_pet}")
    assert response_get.status_code == 200, f"Failed to get updated pet, status code: {response_get.status_code}"
    response = requests.put(u.URL_PET, headers=u.HEADERS, json=pp.UPDATE_PET)
    if response.status_code == 200:
        try:
            validate(instance=response_get.json(), schema=rs.RESPONSE_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")
        assert response_get.json() == pp.UPDATE_PET
    else:
        pytest.fail(f"Pet update failed, status code: {response.status_code}")
