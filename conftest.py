import pytest
import requests
from data_for_tests.url_headers import HEADERS, URL_USER, URL_STORE, URL_PET
from data_for_tests.user_create_payload import CORRECT_ONE_USER_PAYLOAD, USER_PAYLOADS, \
    CORRECT_USER_PAYLOADS
from data_for_tests.store_create_payload import VALID_ONE_PET_PAYLOAD, INVALID_ORDER_PAYLOADS, PET_INVENTORY_TEST_STATUS


@pytest.fixture(params=[f"{URL_USER}/createWithList", f"{URL_USER}/createWithArray"])
def endpoint_url(request):
    return request.param


@pytest.fixture(scope="module")
def valid_username_create():
    url = f"{URL_USER}/createWithList"
    response = requests.post(url, headers=HEADERS, json=[CORRECT_ONE_USER_PAYLOAD])
    if response.status_code == 200:
        username = "testuser1"
        return username
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")


@pytest.fixture(scope="module")
def invalid_username():
    username = "username1"
    return username


@pytest.fixture(scope="module")
def valid_login():
    url = f"{URL_USER}/login?username=testuser1&password=password1"
    return url


@pytest.fixture(scope="module")
def invalid_login():
    url = f"{URL_USER}/login?username=username1&password=gsdfgsdfg"
    return url


@pytest.fixture(scope="module")
def valid_login_user(valid_login):
    url = valid_login
    response = requests.get(url, headers=HEADERS, json={})
    return response.status_code


@pytest.fixture(params=USER_PAYLOADS, ids=[x[0] for x in USER_PAYLOADS])
def user_payload(request):
    return request.param[1]


@pytest.fixture(params=CORRECT_USER_PAYLOADS, ids=[x[0] for x in CORRECT_USER_PAYLOADS])
def user_payload_correct(request):
    return request.param[1]


# TATJANA's
@pytest.fixture(scope="module")
def valid_order_create():
    url = f"{URL_STORE}/order"
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
    absent_id = 14
    return absent_id


@pytest.fixture(scope="module")
def valid_pet_inventory_status():
    url = f"{URL_PET}"
    response = requests.post(url, headers=HEADERS, json=PET_INVENTORY_TEST_STATUS)
    if response.status_code == 200:
        response_json = response.json()
        pet_status = response_json.get("status")
        return pet_status
    else:
        pytest.fail(f"Failed to create a pet, status code: {response.status_code}")
