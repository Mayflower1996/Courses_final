import pytest
import requests
from data.url_headers import URL_PET, HEADERS
from jsonschema.validators import validate
from data.response_schema import RESPONSE_SCHEMA

def test_upload_valid_image_for_pet(image_file_path):
    url = f"{URL_PET}/{image_file_path}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        validate(instance=response.json(), schema=RESPONSE_SCHEMA)
    else:
        pytest.fail(f"Adding image to pet data failed, status code: {response.status_code}")
