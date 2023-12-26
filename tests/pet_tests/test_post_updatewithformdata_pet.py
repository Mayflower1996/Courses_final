import pytest
import requests
from data_for_tests.pet_create_payload import PetPayload as pp
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs


def test_update_pet_data_with_valid_form_data(update_pet_valid_formdata):
    url = f"{u.URL_PET}/{update_pet_valid_formdata}"
    response = requests.get(url, headers=u.HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with formData failed, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == pp.UPDATE_PET_DATA_RESP["name"]
    assert resp["status"] == pp.UPDATE_PET_DATA_RESP["status"]


def test_update_pet_data_invalid_form_data_status(update_pet_invalid_formdata_status):
    url = f"{u.URL_PET}/{update_pet_invalid_formdata_status}"
    response = requests.get(url, headers=u.HEADERS)
    if response.status_code != 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with invalid formData status was successful, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == pp.UPDATE_PET_DATA_RESP["name"]
    assert resp["status"] == pp.UPDATE_PET_DATA_RESP_INVALID["status"]


def test_update_pet_data_invalid_form_data_name(update_pet_formdata_name):
    url = f"{u.URL_PET}/{update_pet_formdata_name}"
    response = requests.get(url, headers=u.HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with formData name failed, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == pp.UPDATE_PET_DATA_RESP_NAME["name"]
    assert resp["status"] == pp.UPDATE_PET_DATA_RESP["status"]
