import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs


def test_get_inventory(valid_pet_inventory_status):
    url = f"{u.URL_STORE}/inventory"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert valid_pet_inventory_status in response.json()
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get valid pet inventories by status, status code: {response.status_code}")
