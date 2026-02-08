
import requests
import time
import sys

BASE_URL = "http://127.0.0.1:5000/api"

def wait_for_server(retries=10, delay=2):
    print(f"Waiting for server at {BASE_URL}...")
    for i in range(retries):
        try:
            resp = requests.get(f"{BASE_URL}/health")
            if resp.status_code == 200:
                print("[OK] Server is UP!")
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(delay)
    print("X Server failed to start.")
    return False

def test_health():
    try:
        resp = requests.get(f"{BASE_URL}/health")
        data = resp.json()
        print(f"Health Check: {resp.status_code} - {data}")
        if resp.status_code == 200 and data['status'] == 'ok':
            return True
    except Exception as e:
        print(f"Health check failed: {e}")
    return False

def test_chat():
    print("Testing Chat Endpoint...")
    payload = {"message": "Hello from verification script", "session_id": "verify_test_1"}
    try:
        resp = requests.post(f"{BASE_URL}/chat", json=payload)
        data = resp.json()
        print(f"Chat Response: {resp.status_code}")
        
        if resp.status_code == 200:
            print(f"Bot says: {data.get('response')}")
            return True
        else:
            print(f"ERROR: {data}")
            return False
    except Exception as e:
        print(f"Chat test failed: {e}")
    return False

if __name__ == "__main__":
    if not wait_for_server():
        sys.exit(1)
        
    if test_health() and test_chat():
        print("[OK] INTEGRATION TEST PASSED")
        sys.exit(0)
    else:
        print("[FAIL] INTEGRATION TEST FAILED")
        sys.exit(1)
