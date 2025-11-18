import requests

def test_root():
    r = requests.get("http://localhost:8000/")
    assert r.status_code == 200
    assert r.json() == {"message": "CI/CD pipeline working!"}
