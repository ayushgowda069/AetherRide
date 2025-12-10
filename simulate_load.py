import requests
import random
import time

MASTER_URL = "http://localhost:5000"

def get_api_url():
    # Pick a random port
    port = random.randint(8000, 8007)
    # Wake it up via Master Node
    try:
        requests.get(f"{MASTER_URL}/spawn/user")
    except:
        pass
    return f"http://localhost:{port}"

locations = ["Metro Station", "Tech Park", "Mall", "Airport", "Downtown", "Suburb", "University", "Stadium"]
names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan"]

def generate_rides(n=100):
    print(f"Generating {n} rides...")
    for i in range(n):
        data = {
            "user_name": f"{random.choice(names)}_{i+1}",
            "pickup_location": random.choice(locations),
            "destination": random.choice(locations)
        }
        try:
            resp = requests.post(f"{get_api_url()}/ride_request/", json=data)
            if resp.status_code == 200:
                print(f"Ride {i+1}/{n} requested: {data['user_name']}")
            else:
                print(f"Failed to request ride {i+1}: {resp.text}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Small delay to not completely overwhelm if running locally with single thread
        time.sleep(0.05) 

if __name__ == "__main__":
    generate_rides(100)
