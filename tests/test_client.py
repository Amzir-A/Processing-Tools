import pytest 
import requests

@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/clients'


@pytest.fixture
def _client_data():
    return {
        "name": "Test Client",
        "address": "123 Test Street",
        "city": "Testville",
        "zip_code": "12345",
        "province": "Test Province",
        "country": "Test Country",
        "contact_name": "John Doe",
        "contact_phone": "123-456-7890",
        "contact_email": "testclient@example.com"
    }

def test_get_clients(_url):
    url = _url
    headers = {
        'API_KEY': 'a1b2c3d4e5'  
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)

    # Get the status code
    status_code = response.status_code

    # Check if the status code is 200 (OK)
    assert status_code == 200, f"Unexpected status code: {status_code}"

def test_add_client(_url, _client_data):
    url = _url
    headers = {
        'API_KEY': 'a1b2c3d4e5', 
        'Content-Type': 'application/json'
    }

    # Send a POST request to add a new client
    response = requests.post(url, headers=headers, json=_client_data)

    # Get the status code
    status_code = response.status_code

    # Check if the status code is 201 (Created)
    assert status_code == 201, f"Unexpected status code: {status_code}"

    # Verify the client was added by sending a GET request
    response = requests.get(url, headers=headers)
    clients = response.json()

    # Check if the new client is in the list of clients
    assert any(client['name'] == _client_data['name'] for client in clients), "Client was not added"