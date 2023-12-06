import pytest
import requests
from data.url_headers import HEADERS, URL_USER, URL_PET
from data.user_create_payload import CORRECT_ONE_USER_PAYLOAD, USER_PAYLOADS, \
    CORRECT_USER_PAYLOADS
from data.pet_create_payload import CORRECT_ONE_PET_PAYLOAD, CORRECT_TWO_PET_PAYLOAD, CORRECT_THREE_PET_PAYLOAD, \
    INCORRECT_STATUS_PET_PAYLOAD


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


@pytest.fixture
def endpoint_url():
    return URL_PET


@pytest.fixture
def headers():
    return HEADERS


@pytest.fixture
def new_pet_data():
    response = requests.post(URL_PET, headers=HEADERS, json=[CORRECT_ONE_PET_PAYLOAD])
    if response.status_code == 200:
        return
    else:
        print(response.content)
        pytest.fail(f"Failed to create a pet, status code: {response.status_code}")


@pytest.fixture
def update_pet_data():
    response = requests.put(URL_PET, headers=HEADERS, json=[CORRECT_TWO_PET_PAYLOAD])
    if response.status_code == 200:
        name = "Tricky"
        photoUrls = "https://upload.wikimedia.org/wikipedia/commons/6/62/Panthera_tigris_sumatran_subspecies.jpg"
        return name, photoUrls
    else:
        pytest.fail(f"Failed to update a pet, status code: {response.status_code}")


@pytest.fixture
def existing_pet_id():
    return [22, 24, 2502]


@pytest.fixture
def pet_status():
    return ["available", "pending", "sold"]


@pytest.fixture
def update_pet_formdata(existing_pet_id):
    pet_id = existing_pet_id[1]
    url = f'{URL_PET}/{pet_id}'
    response = requests.put(url, headers=HEADERS, json=[CORRECT_THREE_PET_PAYLOAD])
    if response.status_code == 200:
        name = "Tortik",
        status = pet_status[2]
        return name, status
    else:
        pytest.fail(f"Failed to update a pet with form data, status code: {response.status_code}")
