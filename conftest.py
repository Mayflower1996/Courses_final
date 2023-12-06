import pytest
import requests
from Tests.pet_tests_and_data.pet_data.url_headers import HEADERS, URL
from Tests.pet_tests_and_data.pet_data.pet_create_payload import CORRECT_ONE_PET_PAYLOAD, CORRECT_TWO_PET_PAYLOAD, CORRECT_THREE_PET_PAYLOAD


@pytest.fixture
def endpoint_url():
    return URL


@pytest.fixture
def headers():
    return HEADERS


@pytest.fixture
def new_pet_data():
    response = requests.post(URL, headers=HEADERS, json=[CORRECT_ONE_PET_PAYLOAD])
    if response.status_code == 200:
        return
    else:
        print(response.content)
        pytest.fail(f"Failed to create a pet, status code: {response.status_code}")


@pytest.fixture
def update_pet_data():
    response = requests.put(URL, headers=HEADERS, json=[CORRECT_TWO_PET_PAYLOAD])
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
    url = f'{URL}/{pet_id}'
    response = requests.put(url, headers=HEADERS, json=[CORRECT_THREE_PET_PAYLOAD])
    if response.status_code == 200:
        name = "Tortik",
        status = pet_status[2]
        return name, status
    else:
        pytest.fail(f"Failed to update a pet with form data, status code: {response.status_code}")

