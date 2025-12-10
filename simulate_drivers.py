import requests
import time
import random

MASTER_URL = "http://localhost:5000"

def get_api_url():
    # Pick a random port
    port = random.randint(7000, 7007)
    # Wake it up via Master Node (this ensures it's running)
    try:
        requests.get(f"{MASTER_URL}/spawn/driver")
    except:
        pass # If master is down, we just try the port anyway
    return f"http://localhost:{port}"

def get_drivers():
    resp = requests.get(f"{get_api_url()}/drivers")
    return resp.json()

def get_pending_rides():
    resp = requests.get(f"{get_api_url()}/rides?status=PENDING")
    return resp.json()

def simulate_driver_action():
    while True:
        drivers = get_drivers()
        available_drivers = [d for d in drivers if d['status'] == 'AVAILABLE']
        
        if not available_drivers:
            print("No drivers available. Waiting...")
            # Check if any driver is busy and complete their ride
            busy_drivers = [d for d in drivers if d['status'] == 'BUSY']
            for driver in busy_drivers:
                # Find their assigned ride
                resp = requests.get(f"{get_api_url()}/driver/{driver['id']}/assigned_ride")
                ride = resp.json()
                if ride:
                    print(f"Driver {driver['name']} completing ride {ride['id']}...")
                    requests.post(f"{get_api_url()}/complete_ride/{ride['id']}")
                    time.sleep(0.5) # Simulate drive time
            time.sleep(1)
            continue

        pending_rides = get_pending_rides()
        if not pending_rides:
            print("No pending rides. Waiting...")
            time.sleep(2)
            continue

        # Assign first pending ride to first available driver
        ride = pending_rides[0]
        driver = available_drivers[0]
        
        print(f"Driver {driver['name']} accepting ride {ride['id']}...")
        resp = requests.post(f"{get_api_url()}/accept_ride/{ride['id']}?driver_id={driver['id']}")
        
        if resp.status_code != 200:
            print(f"Failed to accept: {resp.text}")
        
        time.sleep(0.2)

if __name__ == "__main__":
    print("Starting driver simulation...")
    simulate_driver_action()
