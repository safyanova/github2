import requests
import pytest

@pytest.mark.regression
def test_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    assert response.status_code == 200
    data = response.json()
    assert "setup" in data
    assert "punchline" in data
    print(f"Joke: {data['setup']} - {data['punchline']}")

@pytest.mark.smoke
def test_joke_api_status():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    assert response.status_code == 200