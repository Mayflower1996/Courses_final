import pytest
import requests
from jsonschema.validators import validate
from user_data.url_headers import URL, HEADERS
from user_data.user_get_schema import RESPONSE_SCHEMA


@pytest.mark.order(14)
def test_logout_user(good_login_user):
    if good_login_user == 200:
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
        pytest.fail(f"User login failed with status code: {good_login_user}")
