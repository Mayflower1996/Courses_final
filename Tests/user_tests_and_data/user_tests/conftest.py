import pytest
import requests
from user_data.url_headers_auth_token import URL, HEADERS
from user_data.user_create_payload import CORRECT_ONE_USER_PAYLOAD, USER_PAYLOADS


@pytest.fixture(params=[f"{URL}/createWithArray", f"{URL}/createWithList"])
def endpoint_url(request):
    return request.param


@pytest.fixture(scope="module")
def good_username_create():
    url = f"{URL}/createWithArray"
    response = requests.post(url, headers=HEADERS, json=[CORRECT_ONE_USER_PAYLOAD])
    if response.status_code == 200:
        username = "testuser1"
        return username
    else:
        pytest.fail(f"Failed to create user, status code: {response.status_code}")


@pytest.fixture(scope="module")
def bad_username():
    username = "username1"
    return username


@pytest.fixture(scope="module")
def good_login():
    url = f"{URL}/login?username=testuser1&password=password1"
    return url


@pytest.fixture(scope="module")
def bad_login():
    url = f"{URL}/login?username=username1&password=gsdfgsdfg"
    return url


@pytest.fixture(scope="module")
def good_login_user(good_login):
    url = good_login
    response = requests.get(url, headers=HEADERS, json={})
    return response.status_code


@pytest.fixture(params=USER_PAYLOADS, ids=[x[0] for x in USER_PAYLOADS])
def user_payload(request):
    return request.param[1]
