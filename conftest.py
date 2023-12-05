import pytest
import requests
from Tests.user_tests_and_data.user_data.url_headers import HEADERS, URL_USER
from Tests.user_tests_and_data.user_data.user_create_payload import CORRECT_ONE_USER_PAYLOAD, USER_PAYLOADS, \
    CORRECT_USER_PAYLOADS


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
