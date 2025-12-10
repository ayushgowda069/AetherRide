try:
    print("[1/4] Checking Imports...")
    from AETHER_RIDE import main, models, database
    print("✅ Imports successful.")
except ImportError as e:
    print(f"❌ Import Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected Error during import: {e}")
    sys.exit(1)

from sqlalchemy import text

try:
    print("[2/4] Checking Database Connection...")
    db = database.SessionLocal()
    db.execute(text("SELECT 1"))
    print("✅ Database connected.")
except Exception as e:
    print(f"❌ Database Connection Error: {e}")
    sys.exit(1)

try:
    print("[3/4] Checking Schema (Fare Column)...")
    # Check if 'fare' column exists in 'rides' table
    result = db.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name='rides' AND column_name='fare'"))
    if result.fetchone():
        print("✅ 'fare' column exists.")
    else:
        print("❌ 'fare' column MISSING in 'rides' table.")
except Exception as e:
    print(f"❌ Schema Check Error: {e}")

try:
    print("[4/4] Checking Drivers...")
    drivers = db.query(models.Driver).all()
    print(f"✅ Found {len(drivers)} drivers.")
    for d in drivers:
        print(f"   - {d.name} ({d.status})")
except Exception as e:
    print(f"❌ Driver Check Error: {e}")

db.close()
print("\n=== Diagnostic Complete: SYSTEM HEALTHY ===")
