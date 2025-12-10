from AetherRide import database, models
from sqlalchemy.orm import Session

def clear_rides():
    db = database.SessionLocal()
    
    try:
        # 1. Delete all rides
        num_rides = db.query(models.Ride).delete()
        print(f"Deleted {num_rides} rides.")
        
        # 2. Reset all drivers to AVAILABLE
        drivers = db.query(models.Driver).all()
        for driver in drivers:
            driver.status = models.DriverStatus.AVAILABLE
        
        db.commit()
        print(f"Reset status for {len(drivers)} drivers to AVAILABLE.")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    clear_rides()
