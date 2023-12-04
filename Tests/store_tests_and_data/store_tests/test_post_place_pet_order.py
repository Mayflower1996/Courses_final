import pytest
import requests
from jsonschema.validators import validate
from ..store_data.url_headers import URL, HEADERS
from ..store_data.store_get_schema import RESPONSE_SCHEMA
from ..store_data.store_create_payload import VALID_ONE_PET_PAYLOAD, INVALID_TWO_PETS_PAYLOAD


def test_place_pet_order():
    url = f"{URL}/order"
    response = requests.post(url, headers=HEADERS, json=VALID_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order failed, status code: {response.status_code}")


@pytest.mark.xfail(reason="2 instances at once are not processed.")
def test_place_pet_two_orders():
    # expected fail
    url = f"{URL}/order"
    response = requests.post(url, headers=HEADERS, json=INVALID_TWO_PETS_PAYLOAD)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Creating pet order failed, status code: {response.status_code}")


def test_place_invalid_order(order_invalid_payload):
    url = f"{URL}/order"
    response = requests.post(url, headers=HEADERS, json=order_invalid_payload)
    if response.status_code == 500:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        assert "something bad happened" in response.text
    else:
        pytest.fail(f"Creating pet order should fail, but status code: {response.status_code}")
