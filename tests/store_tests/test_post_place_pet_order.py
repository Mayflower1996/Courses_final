import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL_STORE, HEADERS
from data_for_tests.response_schema import RESPONSE_SCHEMA
from data_for_tests.store_create_payload import VALID_ONE_PET_PAYLOAD, INVALID_TWO_PETS_PAYLOAD


def test_place_pet_order():
    url = f"{URL_STORE}/order"
    response = requests.post(url, headers=HEADERS, json=VALID_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order failed, status code: {response.status_code}")


def test_place_pet_two_orders():
    url = f"{URL_STORE}/order"
    response = requests.post(url, headers=HEADERS, json=INVALID_TWO_PETS_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order was successful, status code: {response.status_code}")


def test_place_invalid_order(order_invalid_payload):
    url = f"{URL_STORE}/order"
    response = requests.post(url, headers=HEADERS, json=order_invalid_payload)
    if response.status_code == 500:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        assert "something bad happened" in response.text
    else:
        pytest.fail(f"Creating pet order should fail, but status code: {response.status_code}")
