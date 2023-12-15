import pytest
import requests
from data_for_tests.pet_create_payload import UPDATE_PET_DATA_RESP, UPDATE_PET_DATA_RESP_INVALID, UPDATE_PET_DATA_RESP_NAME
from jsonschema.validators import validate
from data_for_tests.url_headers import URL_PET, HEADERS
from data_for_tests.response_schema import RESPONSE_SCHEMA


def test_update_pet_data_with_valid_form_data(update_pet_valid_formdata):
    url = f"{URL_PET}/{update_pet_valid_formdata}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with formData failed, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == UPDATE_PET_DATA_RESP["name"]
    assert resp["status"] == UPDATE_PET_DATA_RESP["status"]


def test_update_pet_data_invalid_form_data_status(update_pet_invalid_formdata_status):
    url = f"{URL_PET}/{update_pet_invalid_formdata_status}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with invalid formData status was successful, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == UPDATE_PET_DATA_RESP["name"]
    assert resp["status"] == UPDATE_PET_DATA_RESP_INVALID["status"]


def test_update_pet_data_invalid_form_data_name(update_pet_formdata_name):
    url = f"{URL_PET}/{update_pet_formdata_name}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Updating pet with formData name failed, status code: {response.status_code}")
    resp = response.json()
    assert resp["name"] == UPDATE_PET_DATA_RESP_NAME["name"]
    assert resp["status"] == UPDATE_PET_DATA_RESP["status"]
