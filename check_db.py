from AetherRide import database, models
from sqlalchemy.orm import Session

def check_data():
    db = database.SessionLocal()
    
    print("--- DRIVERS ---")
    drivers = db.query(models.Driver).all()
    for d in drivers:
        print(f"ID: {d.id}, Name: {d.name}, Status: {d.status}")
        
    print("\n--- RIDES ---")
    rides = db.query(models.Ride).all()
    for r in rides:
        print(f"ID: {r.id}, User: {r.user_name}, Status: {r.status}, Driver: {r.driver_id}")
        
    db.close()

if __name__ == "__main__":
    check_data()
