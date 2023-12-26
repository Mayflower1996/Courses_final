import pytest
import requests
from jsonschema.validators import validate
from data_for_tests.url_headers import URL as u
from data_for_tests.response_schema import ResponseSchema as rs


def test_delete_order(valid_order_create):
    url = f"{u.URL_STORE}/order/{valid_order_create}"
    response = requests.delete(url, headers=u.HEADERS, json={})
    if response.status_code == 200:
        assert "200" in response.text
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
        deleted_check = requests.get(url)
        assert deleted_check.status_code == 404
    else:
        pytest.fail(f"Failed to delete order by ID, status code: {response.status_code}")


def test_delete_invalid_order(absent_order):
    url = f"{u.URL_STORE}/order/{absent_order}"
    response = requests.delete(url, headers=u.HEADERS, json={})
    assert response.status_code == 404
    validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)


def test_delete_no_orderid():
    url = f"{u.URL_STORE}/order"
    response = requests.delete(url, headers=u.HEADERS, json={})
    assert response.status_code == 400 or 405
    assert "unknown" in response.text
