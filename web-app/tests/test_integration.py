import requests
import json

def test_hello(url):
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == "Hello, World!"