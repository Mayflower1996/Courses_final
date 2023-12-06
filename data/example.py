# test_pet.py
import pytest
import requests

def test_create_new_pet(base_url, headers, new_pet_data):
    response = requests.post(f'{base_url}/pet', headers=headers, json=new_pet_data)
    assert response.status_code == 200
    assert response.json() == new_pet_data

def test_update_existing_pet(base_url, headers, update_pet_data, existing_pet_id):
    response = requests.put(f'{base_url}/pet/{existing_pet_id}', headers=headers, json=update_pet_data)
    assert response.status_code == 200
    assert response.json() == update_pet_data

def test_get_pet_by_id(base_url, headers, existing_pet_id):
    response = requests.get(f'{base_url}/pet/{existing_pet_id}', headers=headers)
    assert response.status_code == 200
    # Add more assertions based on the expected response

def test_find_pet_by_status(base_url, headers, pet_status):
    params = {'status': ','.join(pet_status)}
    response = requests.get(f'{base_url}/pet/findByStatus', headers=headers, params=params)
    assert response.status_code == 200
    # Add more assertions based on the expected response

def test_update_pet_with_formdata(base_url, headers, existing_pet_id, update_pet_formdata):
    params = {'name': update_pet_formdata['name'], 'status': update_pet_formdata['status']}
    response = requests.post(f'{base_url}/pet/{existing_pet_id}', headers=headers, data=params)
    assert response.status_code == 200
    # Add more assertions based on the expected response

def test_delete_pet(base_url, headers, existing_pet_id, api_key):
    headers['api_key'] = api_key
    response = requests.delete(f'{base_url}/pet/{existing_pet_id}', headers=headers)
    assert response.status_code == 200
    # Add more assertions based on the expected response
