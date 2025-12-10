import time
import os
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# Database Connection
password = quote_plus("Ayushgowda@123")
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/AETHER_DATABASE"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def watch_transactions():
    print("👀 Watching Database for Transitions... (Press Ctrl+C to stop)")
    print("-" * 60)
    print(f"{'TIME':<10} | {'RIDE ID':<8} | {'USER':<15} | {'STATUS':<10} | {'DRIVER'}")
    print("-" * 60)

    last_seen_status = {}

    while True:
        try:
            with engine.connect() as connection:
                # Get all rides
                result = connection.execute(text("SELECT id, user_name, status, driver_id FROM rides ORDER BY id DESC LIMIT 20"))
                rows = result.fetchall()

                for row in rows:
                    ride_id = row[0]
                    user = row[1]
                    status = row[2]
                    driver_id = row[3]
                    
                    # Create a unique key for the state
                    current_state = f"{status}_{driver_id}"

                    # If we haven't seen this ride, or its status changed
                    if ride_id not in last_seen_status:
                        last_seen_status[ride_id] = current_state
                        # Don't print initial load to keep it clean, only new updates
                        # (Optional: remove this check if you want to see current state on start)
                    
                    elif last_seen_status[ride_id] != current_state:
                        # STATUS CHANGED!
                        timestamp = time.strftime("%H:%M:%S")
                        driver_str = f"Driver {driver_id}" if driver_id else "Searching..."
                        
                        # Color coding
                        color = ""
                        if status == "ACCEPTED": color = "\033[93m" # Yellow
                        elif status == "COMPLETED": color = "\033[92m" # Green
                        elif status == "PENDING": color = "\033[96m" # Cyan
                        reset = "\033[0m"

                        print(f"{timestamp:<10} | {ride_id:<8} | {user:<15} | {color}{status:<10}{reset} | {driver_str}")
                        
                        last_seen_status[ride_id] = current_state

            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    # Enable colors in Windows terminal
    os.system('color')
    watch_transactions()
