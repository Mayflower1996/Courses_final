import pytest
import requests
from ..store_data.url_headers import URL, HEADERS
from ..store_data.store_create_payload import VALID_ONE_PET_PAYLOAD, INVALID_ORDER_PAYLOADS


@pytest.fixture(scope="module")
def valid_order_create():
    url = f"{URL}/order"
    response = requests.post(url, headers=HEADERS, json=VALID_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        response_json = response.json()
        order_id = response_json.get("id")
        return order_id
    else:
        pytest.fail(f"Failed to create order, status code: {response.status_code}")


@pytest.fixture(params=INVALID_ORDER_PAYLOADS, ids=[x[0] for x in INVALID_ORDER_PAYLOADS])
def order_invalid_payload(request):
    return request.param[1]


@pytest.fixture(scope="module")
def absent_order():
    absent_id = 9
    return absent_id
