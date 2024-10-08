import requests
import pytest

BASE_URL = "http://localhost:3000/api/v1/Clients"
API_KEY = "a1b2c3d4e5"  
HEADERS = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

@pytest.fixture
def new_client_data():
    """Fixture voor het creëren van een nieuwe client."""
    return {
        "name": "Testbedrijf BV",
        "address": "Straatnaam 123",
        "city": "Teststad",
        "zip_code": "1234AB",
        "province": "Testprovincie",
        "country": "Nederland",
        "contact_name": "Jan Tester",
        "contact_phone": "+31123456789",
        "contact_email": "jan@testbedrijf.nl"
    }

def log_response(response):
    """Hulpmethode om de response-informatie te loggen voor debugging."""
    print(f"Request URL: {response.url}")
    print(f"Request Headers: {HEADERS}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

def test_get_all_clients():
    """Test om alle cliënten op te halen."""
    response = requests.get(BASE_URL, headers=HEADERS)
    log_response(response)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response is not a list"
    print("Alle cliënten succesvol opgehaald.")

def test_add_new_client(new_client_data):
    """Test om een nieuwe cliënt toe te voegen en te controleren."""
    # Voeg een nieuwe cliënt toe
    response = requests.post(BASE_URL, json=new_client_data, headers=HEADERS)
    log_response(response)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

    # Haal alle cliënten opnieuw op om te controleren of de nieuwe cliënt is toegevoegd
    response = requests.get(BASE_URL, headers=HEADERS)
    log_response(response)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    clients = response.json()
    assert any(client['name'] == new_client_data["name"] for client in clients), "Nieuwe cliënt niet gevonden in de lijst."
    print("Nieuwe cliënt succesvol toegevoegd en geverifieerd.")
