import requests
import pytest

URL_BASE= "http://localhost:8000"

def test_read_root():
    url = f"{URL_BASE}/"
    response = requests.get(url)
    assert response.status_code == 202
    assert response.json() == {"message": "Pruebas unitarias"}

def test_sumas():
    url = f"{URL_BASE}/sumas"
    params = {"numero1": 5, "numero2": 10}
    response = requests.get(url, params=params)
    assert response.status_code == 202
    assert response.json() == {"numero1": 5, "numero2": 10, "suma": 15}