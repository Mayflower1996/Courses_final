import pytest
import requests
from jsonschema.validators import validate
from data.url_headers import URL_STORE
from data.response_schema import RESPONSE_SCHEMA


def test_get_inventory(valid_pet_inventory_status):
    url = f"{URL_STORE}/inventory"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert valid_pet_inventory_status in response.json()
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get valid pet inventories by status, status code: {response.status_code}")
