import pytest
import requests
from jsonschema.validators import validate
from url_headers import URL, HEADERS
from pet_get_schema import RESPONSE_SCHEMA


def test_create_pet_success(CORRECT_ONE_PET_PAYLOAD):
    response = requests.post(f"{URL}", json=sample_pet_data)

    assert response.status_code == 200
    assert response.json()["name"] == "doggie"
    assert response.json()["status"] == "available"


def test_create_pet_validation_error():
    invalid_pet_data = {
        # Invalid data, missing required fields, etc.
    }
    response = requests.post(f"{API_BASE_URL}/pet", json=invalid_pet_data)

    assert response.status_code == 400
    assert "error" in response.json()


def test_created_pet_exists(sample_pet_data):
    response = requests.post(f"{API_BASE_URL}/pet", json=sample_pet_data)
    created_pet_id = response.json()["id"]

    # Make a separate request to fetch the created pet by ID
    fetch_response = requests.get(f"{API_BASE_URL}/pet/{created_pet_id}")

    assert fetch_response.status_code == 200
    assert fetch_response.json()["name"] == "doggie"
    assert fetch_response.json()["status"] == "available"