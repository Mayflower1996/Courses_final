import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs
from data_for_tests.store_create_payload import StorePayload as sp


def test_place_pet_order():
    url = f"{u.URL_STORE}/order"
    response = requests.post(url, headers=u.HEADERS, json=sp.VALID_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order failed, status code: {response.status_code}")


def test_place_pet_two_orders():
    url = f"{u.URL_STORE}/order"
    response = requests.post(url, headers=u.HEADERS, json=sp.INVALID_TWO_PETS_PAYLOAD)
    if response.status_code != 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order was successful, status code: {response.status_code}")


def test_place_invalid_order(order_invalid_payload):
    url = f"{u.URL_STORE}/order"
    response = requests.post(url, headers=u.HEADERS, json=order_invalid_payload)
    if response.status_code == 500:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
        assert "something bad happened" in response.text
    else:
        pytest.fail(f"Creating pet order should fail, but status code: {response.status_code}")
