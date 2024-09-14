import pytest 
import requests
from src.feed import get_feed, get_user

def test_get_feed(monkeypatch):
    data =  '''
    <h1>Title</h1>
    <p>Sample paragram that explains the title</p>
    '''
    def mock_delay():
        print('no delay') 
    
    monkeypatch.setattr('src.feed.delay', mock_delay)

    assert get_feed() == data

def test_get_user(monkeypatch):
    data = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
            }
        },
    }
    class MockUser:
        def __init__(self):
            self.status_code = 200
            self.url = 'http://get_user.com'
        def json(self):
            return data

    def mock_get(*args, **kwargs):
        return MockUser()

    monkeypatch.setattr('requests.get', mock_get)
    # assert r.name == 'Leane Graham'
    assert get_user(1)['name'] == 'Leanne Graham'