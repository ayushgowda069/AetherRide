import requests

API_URL = "http://localhost:8000"
DRIVER_ID = 4

def check_api():
    print(f"Checking API for Driver {DRIVER_ID}...")
    try:
        resp = requests.get(f"{API_URL}/driver/{DRIVER_ID}/assigned_ride")
        if resp.status_code == 200:
            data = resp.json()
            if data:
                print("SUCCESS! API returned ride:")
                print(data)
            else:
                print("API returned null (No assigned ride found via API).")
        else:
            print(f"API Error: {resp.status_code}")
            print(resp.text)
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    check_api()
