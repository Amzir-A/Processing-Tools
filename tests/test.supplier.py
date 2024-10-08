import pytest
import requests

@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/suppliers'


@pytest.fixture
def _supplier_data():
    return {
        "code": "SUP0497",
        "name": "Neal-Hoffman",
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

def test_get_suppliers(_url):
    url = _url
    headers = {
        'API_KEY': 'a1b2c3d4e5'  # Zorg ervoor dat deze API-sleutel geldig is en toegang heeft tot de endpoint
    }

    # Verzend een GET-verzoek naar de API
    response = requests.get(url, headers=headers)

    # Controleer of de statuscode 200 is
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

def test_add_supplier(_url, _supplier_data):
    url = _url
    headers = {
        'API_KEY': 'a1b2c3d4e5',  # Zorg ervoor dat deze API-sleutel geldig is en toegang heeft tot de endpoint
        'Content-Type': 'application/json'
    }

    # Verzend een POST-verzoek om een nieuwe leverancier toe te voegen
    response = requests.post(url, headers=headers, json=_supplier_data)

    # Controleer of de statuscode 201 (Created) is
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # Verifieer dat er een GET-verzoek kan worden uitgevoerd om leveranciers op te halen
    response = requests.get(url, headers=headers)

    # Controleer of de statuscode 200 is
    assert response.status_code == 200, f"Unexpected status code when fetching suppliers: {response.status_code}"
