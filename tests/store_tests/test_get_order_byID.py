import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.store_get_schema import OrderSchema as ords
from data_for_tests.response_schema import ResponseSchema as rs


def test_get_valid_order(valid_order_create):
    url = f"{u.URL_STORE}/order/{valid_order_create}"
    response = requests.get(url)
    if response.status_code == 200:
        assert response.status_code == 200
        assert "id" in response.json()
        validate(instance=response.json(), schema=ords.ORDER_GET_VALID_RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Can't get order by ID, status code: {response.status_code}")


def test_get_invalid_order(absent_order):
    url = f"{u.URL_STORE}/order/{absent_order}"
    response = requests.get(url)
    if response.status_code == 404:
        assert "Order not found" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"ORDER with ID {absent_order} exists, status code: {response.status_code}")


def test_no_orderid():
    url = f"{u.URL_STORE}/order/"
    response = requests.get(url)
    if response.status_code == 405 or 400:
        assert "unknown" in response.text
    else:
        pytest.fail(f"Empty ID exists, status code: {response.status_code}")
