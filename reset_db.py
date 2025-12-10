from AETHER_RIDE import database, models

def reset_db():
    print("Dropping all tables...")
    models.Base.metadata.drop_all(bind=database.engine)
    print("Creating all tables...")
    models.Base.metadata.create_all(bind=database.engine)
    print("Database reset complete.")

if __name__ == "__main__":
    reset_db()
