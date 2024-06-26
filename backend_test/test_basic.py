import requests
import pytest

URL = "https://api"
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": ""
}

def test_get_trainers():
    """
    KTI-1. test_get_trainers 
    """
    response = requests.get(url=f'{URL}/v2/trainers',)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():
    """
    KTI-2. test_get_trainers by id
    """
    response = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id': 2978}, timeout=3)
    assert response.status_code == 200, 'Unexpected status code'
    
