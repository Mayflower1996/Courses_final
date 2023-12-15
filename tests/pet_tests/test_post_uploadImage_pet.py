import pytest
import requests
from data_for_tests.url_headers import URL as u
from jsonschema.validators import validate
from data_for_tests.response_schema import ResponseSchema as rs


def test_upload_valid_image_for_pet(image_file_path):
    url = f"{u.URL_PET}/{image_file_path}"
    response = requests.get(url, headers=u.HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=rs.RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Adding image to pet data failed, status code: {response.status_code}")
