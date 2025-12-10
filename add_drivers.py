from AetherRide import database, models

def add_drivers():
    db = database.SessionLocal()
    
    new_drivers = [
        "Rohan", "Vikram", "Suresh", "Rahul", "Amit", 
        "Karan", "Nikhil", "Deepak", "Sanjay", "Anil",
        "Rajesh", "Manoj"
    ]
    
    print(f"Adding {len(new_drivers)} new drivers...")
    for name in new_drivers:
        # Check if exists to avoid duplicates if run multiple times
        exists = db.query(models.Driver).filter(models.Driver.name == name).first()
        if not exists:
            driver = models.Driver(name=name, status=models.DriverStatus.AVAILABLE)
            db.add(driver)
            print(f"Added {name}")
        else:
            print(f"Skipping {name} (already exists)")

    db.commit()
    db.close()

if __name__ == "__main__":
    add_drivers()
