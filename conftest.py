import os
import pytest
import requests
from data_for_tests.url_headers import URL as u
from data_for_tests.user_create_payload import UserPayload as up
from data_for_tests.pet_create_payload import PetPayload as pp
from data_for_tests.store_create_payload import StorePayload as sp


@pytest.fixture(params=[f"{u.URL_USER}/createWithList", f"{u.URL_USER}/createWithArray"])
def endpoint_url(request):
    return request.param


@pytest.fixture(scope="module")
def valid_username_create():
    url = f"{u.URL_USER}/createWithList"
    response = requests.post(url, headers=u.HEADERS, json=[up.CORRECT_ONE_USER_PAYLOAD])
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
    url = f"{u.URL_USER}/login?username=testuser1&password=password1"
    return url


@pytest.fixture(scope="module")
def invalid_login():
    url = f"{u.URL_USER}/login?username=username1&password=gsdfgsdfg"
    return url


@pytest.fixture(scope="module")
def valid_login_user(valid_login):
    url = valid_login
    response = requests.get(url, headers=u.HEADERS, json={})
    return response.status_code


@pytest.fixture(params=up.USER_PAYLOADS, ids=[x[0] for x in up.USER_PAYLOADS])
def user_payload(request):
    return request.param[1]


@pytest.fixture(params=up.CORRECT_USER_PAYLOADS, ids=[x[0] for x in up.CORRECT_USER_PAYLOADS])
def user_payload_correct(request):
    return request.param[1]


# TATJANA's
@pytest.fixture(scope="module")
def valid_order_create():
    url = f"{u.URL_STORE}/order"
    response = requests.post(url, headers=u.HEADERS, json=sp.VALID_ONE_PET_PAYLOAD)
    if response.status_code == 200:
        response_json = response.json()
        order_id = response_json.get("id")
        return order_id
    else:
        pytest.fail(f"Failed to create order, status code: {response.status_code}")


@pytest.fixture(params=sp.INVALID_ORDER_PAYLOADS, ids=[x[0] for x in sp.INVALID_ORDER_PAYLOADS])
def order_invalid_payload(request):
    return request.param[1]


@pytest.fixture(scope="module")
def absent_order():
    absent_id = 14
    return absent_id


@pytest.fixture(scope="module")
def valid_pet_inventory_status():
    url = f"{u.URL_PET}"
    response = requests.post(url, headers=u.HEADERS, json=sp.PET_INVENTORY_TEST_STATUS)
    if response.status_code == 200:
        response_json = response.json()
        pet_status = response_json.get("status")
        return pet_status
    else:
        pytest.fail(f"Failed to create a pet, status code: {response.status_code}")


# Yuliya's
@pytest.fixture
def new_pet_data():
    response = requests.post(u.URL_PET, headers=u.HEADERS, json=pp.CORRECT_FOUR_PET_PAYLOAD)
    if response.status_code == 200:
        response_json = response.json()
        pet_id = response_json.get("id")
        return pet_id
    else:
        pytest.fail(f"Failed to create a pet, status code: {response.status_code}")


@pytest.fixture
def create_and_update_pet():
    create_response = requests.post(u.URL_PET, headers=u.HEADERS, json=pp.CORRECT_FOUR_PET_PAYLOAD)
    create_response.raise_for_status()
    pet_id = create_response.json()["id"]
    update_response = requests.put(u.URL_PET, headers=u.HEADERS, json=pp.UPDATE_PET)
    update_response.raise_for_status()
    return pet_id


@pytest.fixture
def not_existing_pet_id():
    pet_id = 4536720000900900000037264
    return pet_id


@pytest.fixture
def pet_statuses():
    status_list = ["available", "pending", "sold"]
    return status_list


@pytest.fixture
def invalid_pet_status():
    status_invalid = "nosuchstatus"
    return status_invalid


@pytest.fixture
def empty_pet_status():
    status_empty = ""
    return status_empty


@pytest.fixture
def get_pet_data(new_pet_data):
    url = f"{u.URL_PET}/{new_pet_data}"
    response = requests.get(url)
    pet_data = {}
    if response.status_code == 200:
        assert response.status_code == 200
        assert "id" in response.json()
        pet_data = response.json()
    return pet_data


@pytest.fixture
def update_pet_valid_formdata(get_pet_data):
    url = f"{u.URL_PET}/{get_pet_data['id']}"
    response = requests.post(url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
        }, params={"name": pp.UPDATE_PET_DATA_RESP["name"], "status": pp.UPDATE_PET_DATA_RESP["status"]})
    assert response.status_code == 200
    return get_pet_data["id"]


@pytest.fixture
def update_pet_invalid_formdata_status(get_pet_data):
    url = f"{u.URL_PET}/{get_pet_data['id']}"
    response = requests.post(url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
        }, params={"name": pp.UPDATE_PET_DATA_RESP["name"], "status": pp.UPDATE_PET_DATA_RESP_INVALID["status"]})
    assert response.status_code == 200
    return get_pet_data["id"]


@pytest.fixture
def update_pet_formdata_name(get_pet_data):
    url = f"{u.URL_PET}/{get_pet_data['id']}"
    response = requests.post(url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
        }, params={"name": pp.UPDATE_PET_DATA_RESP_NAME["name"], "status": pp.UPDATE_PET_DATA_RESP["status"]})
    assert response.status_code == 200
    return get_pet_data["id"]


@pytest.fixture
def update_pet_formdata_empty(get_pet_data):
    url = f"{u.URL_PET}/{get_pet_data['id']}"
    response = requests.post(url, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
        }, params={"name": '', "status": ''})
    assert response.status_code == 200
    return get_pet_data["id"]


@pytest.fixture
def image_file_path(get_pet_data):
    url = f"{u.URL_PET}/{get_pet_data['id']}/uploadImage"
    image_path = "data_for_tests/Pet_photo.jpg"
    full_path = os.path.join(os.getcwd(), image_path)
    with open(full_path, 'rb') as file:
        image_data = file.read()
    response = requests.post(url, files={'file': image_data})
    assert response.status_code == 200
    return get_pet_data["id"]
