import requests
import time

BASE = "http://127.0.0.1:5000"

def wait_for_up(url, timeout=15):
    end = time.time() + timeout
    while time.time() < end:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False

def test_home_integration():
    # Wait until the service starts
    assert wait_for_up(BASE + "/"), "Server did not start in time"
    r = requests.get(BASE + "/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello from microservice!"}
