import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL_PET, HEADERS
from data_for_tests.response_schema import RESPONSE_SCHEMA
from data_for_tests.pet_create_payload import CORRECT_ONE_PET_PAYLOAD, CORRECT_THREE_PET_PAYLOAD, \
    PET_PAYLOAD_EMPTY_FIELDS, REQUIRED_FIELDS_EMPTY_PET_PAYLOAD, INCORRECT_STATUS_PET_PAYLOAD, \
    LONG_ID_PET_PAYLOAD, INCORRECT_ID1_PET_PAYLOAD, INCORRECT_ID_PET_PAYLOAD


def test_create_pet_success():
    response = requests.post(URL_PET, headers=HEADERS, json=CORRECT_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating a new pet failed, status code: {response.status_code}")


def test_create_pet_validation_error():
    response = requests.post(URL_PET, headers=HEADERS, json=CORRECT_THREE_PET_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating already existed pet in the store was successful, status code: {response.status_code}")


def test_create_pet_without_required_fields():
    response = requests.post(URL_PET, headers=HEADERS, json=REQUIRED_FIELDS_EMPTY_PET_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet without required information was successful, status code: {response.status_code}")


def test_create_pet_without_body():
    response = requests.post(URL_PET, headers=HEADERS, json=PET_PAYLOAD_EMPTY_FIELDS)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet without any information was successful, status code: {response.status_code}")


def test_create_pet_with_incorrect_status():
    response = requests.post(URL_PET, headers=HEADERS, json=INCORRECT_STATUS_PET_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet with incorrect status was successful, status code: {response.status_code}")


def test_create_pet_with_negative_id():
    response = requests.post(URL_PET, headers=HEADERS, json=INCORRECT_ID1_PET_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet with negative ID was successful, status code: {response.status_code}")


def test_create_pet_with_long_id():
    response = requests.post(URL_PET, headers=HEADERS, json=LONG_ID_PET_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet with long ID failed, status code: {response.status_code}")


def test_create_pet_with_incorrect_id():
    response = requests.post(URL_PET, headers=HEADERS, json=INCORRECT_ID_PET_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet with incorrect ID was successful, status code: {response.status_code}")
