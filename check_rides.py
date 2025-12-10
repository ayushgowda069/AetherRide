from AetherRide import database, models
from sqlalchemy.orm import Session

def check_rides():
    db = database.SessionLocal()
    print("=== RIDE CHECK ===")
    rides = db.query(models.Ride).all()
    print(f"Total Rides Found: {len(rides)}")
    for r in rides:
        print(f"ID: {r.id} | User: {r.user_name} | Status: {r.status} | Driver: {r.driver_id}")
    db.close()

if __name__ == "__main__":
    check_rides()
