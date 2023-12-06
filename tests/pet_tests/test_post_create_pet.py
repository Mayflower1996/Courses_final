# import pytest
import requests
# from jsonschema.validators import validate
from data.url_headers import URL, HEADERS
# from pet_get_schema import PET_GET_VALID_RESPONSE_SCHEMA
# from data.pet_create_payload import CORRECT_ONE_PET_PAYLOAD, CORRECT_TWO_PET_PAYLOAD, CORRECT_THREE_PET_PAYLOAD


def test_create_pet_success(new_pet_data):
    assert new_pet_data is not None
    response = requests.get(f"{URL}/{new_pet_data[0]['id']}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["name"] == CORRECT_ONE_PET_PAYLOAD["name"]
    assert response.json()["status"] == CORRECT_ONE_PET_PAYLOAD["status"]

# @pytest.mark.usefixtures("new_pet_data")
# def test_create_pet_success(new_pet_data):
#     created_pet_id = new_pet_data[0]["id"]
#     response = requests.get(f"{URL}/{created_pet_id}")
#
#     assert response.status_code == 200
#     assert response.json()["name"] == "Pushistik"
#     assert response.json()["status"] == "available"


# def test_create_pet_validation_error():
#     invalid_pet_data = {
#         # Invalid data, missing required fields, etc.
#     }
#     response = requests.post(f"{URL}", json=invalid_pet_data, headers=HEADERS)
#
#     assert response.status_code == 400
#     assert "error" in response.json()
#
#
# @pytest.mark.usefixtures("new_pet_data")
# def test_created_pet_exists(new_pet_data):
#     created_pet_id = new_pet_data[0]["id"]
#     response = requests.get(f"{URL}/{created_pet_id}")
#
#     assert response.status_code == 200
#     assert response.json()["name"] == "Pushistik"
#     assert response.json()["status"] == "available"
