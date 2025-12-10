from AETHER_RIDE import database, models
import random

def add_30_drivers():
    db = database.SessionLocal()
    
    first_names = ["Raju", "Farhan", "Rancho", "Chatur", "Virus", "Joy", "Millimeter", "Manav", "Kabir", "Arjun", "Imran", "Zoya", "Sid", "Sameer", "Akash", "Circuit", "Munna", "Babu", "Rao", "Ganesh", "Shiva", "Bheema", "Nakul", "Sahadev", "Karna", "Duryodhan", "Shakuni", "Bhishma", "Drona", "Ashwatthama"]
    
    print("Adding 30 new drivers...")
    count = 0
    for name in first_names:
        # Append a random number to ensure uniqueness if name repeats in future
        full_name = f"{name}_{random.randint(100, 999)}"
        
        driver = models.Driver(name=full_name, status=models.DriverStatus.AVAILABLE)
        db.add(driver)
        print(f"Added {full_name}")
        count += 1
        
    db.commit()
    db.close()
    print(f"✅ Successfully added {count} drivers.")

if __name__ == "__main__":
    add_30_drivers()
