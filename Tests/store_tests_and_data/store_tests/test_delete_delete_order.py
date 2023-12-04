import pytest
import requests
from jsonschema.validators import validate
from ..store_data.url_headers import URL, HEADERS
from ..store_data.store_get_schema import RESPONSE_SCHEMA


def test_delete_order(valid_order_create):
    url = f"{URL}/order/{valid_order_create}"
    response = requests.delete(url, headers=HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Failed to delete order by ID, status code: {response.status_code}")


def test_delete_invalid_order(absent_order):
    url = f"{URL}/order/{absent_order}"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 404
    validate(instance=response.json(), schema=RESPONSE_SCHEMA)


def test_delete_no_orderid():
    url = f"{URL}/order"
    response = requests.delete(url, headers=HEADERS, json={})
    assert response.status_code == 400 or 405
    assert "unknown" in response.text
