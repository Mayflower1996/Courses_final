import pytest
import requests
from jsonschema.validators import validate
from Tests.user_tests_and_data.user_data.url_headers import URL, HEADERS
from Tests.user_tests_and_data.user_data.user_get_schema import RESPONSE_SCHEMA
from Tests.conftest import valid_login_user, valid_login # noqa


@pytest.mark.order(19)
def test_logout_user(valid_login_user, valid_login):
    if valid_login_user == 200:
        url = f"{URL}/logout"
        response = requests.get(url, headers=HEADERS, json={})
        assert response.status_code == 200
        assert "ok" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        url = f"{URL}/logout"
        response = requests.get(url, headers=HEADERS, json={})
        assert response.status_code != 200
        assert "error" in response.text
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
        pytest.fail(f"User login failed, status code: {valid_login_user}")
