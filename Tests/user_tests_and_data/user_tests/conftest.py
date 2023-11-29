import pytest
import requests

from user_data.url_headers_auth_token import URL, HEADERS
from user_data.user_create_payload import CORRECT_ONE_USER_PAYLOAD


@pytest.fixture(params=[f"{URL}/createWithArray", f"{URL}/createWithList"])
def endpoint_url(request):
    return request.param


@pytest.fixture(scope="module")
def good_username():
    username = "string"
    return username


@pytest.fixture(scope="module")
def bad_username():
    username = "username1"
    return username
