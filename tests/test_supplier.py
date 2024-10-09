import pytest
import requests

@pytest.fixture
def _supplier_url():
    return 'http://localhost:3000/api/v1/suppliers'


@pytest.fixture
def _supplier_data():
    return {
        "code": "SUP0497",
        "name": "meneer banaan",
        "address": "7032 Mindy Meadow",
        "address_extra": "Apt. 937",
        "city": "Lake Alex",
        "zip_code": "62913",
        "province": "Washington",
        "country": "Taiwan",
        "contact_name": "Jeffrey Larsen",
        "phonenumber": "(786)666-7146",
        "reference": "N-SUP0497"
    }

def test_get_suppliers(_supplier_url):
    url = _supplier_url
    headers = {
        'API_KEY': 'a1b2c3d4e5' 
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)
    

    # Check if the status code is 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

def test_add_supplier(_supplier_url, _supplier_data):
    url = _supplier_url
    headers = {
        'API_KEY': 'a1b2c3d4e5', 
        'Content-Type': 'application/json'
    }

    # Send a POST request to add a new supplier
    response = requests.post(url, headers=headers, json=_supplier_data)

    # Check if the status code is 201 (Created)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # Verify the supplier was added by sending a GET request
    response = requests.get(url, headers=headers)
    suppliers = response.json()

    # Check if the new supplier is in the list of suppliers
    assert any(supplier['name'] == _supplier_data['name'] for supplier in suppliers), "Supplier was not added"