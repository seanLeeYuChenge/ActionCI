import requests
def test_home():
    r = requests.get("http://127.0.0.1:5001?a=10&b=5")
    assert r.status_code == 200
