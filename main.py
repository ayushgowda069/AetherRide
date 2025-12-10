from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Aether Ride")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="AETHER_RIDE/static"), name="static")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = database.SessionLocal()
    if db.query(models.Driver).count() == 0:
        drivers = [
            models.Driver(name="Arjun", status=models.DriverStatus.AVAILABLE),
            models.Driver(name="Mahesh", status=models.DriverStatus.AVAILABLE),
            models.Driver(name="Pawan", status=models.DriverStatus.AVAILABLE),
        ]
        db.add_all(drivers)
        db.commit()
    db.close()

@app.post("/ride_request/", response_model=schemas.RideResponse)
def create_ride(ride: schemas.RideCreate, db: Session = Depends(get_db)):
    db_ride = models.Ride(**ride.dict(), status=models.RideStatus.PENDING)
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

@app.get("/rides", response_model=List[schemas.RideResponse])
def read_rides(status: Optional[models.RideStatus] = None, db: Session = Depends(get_db)):
    query = db.query(models.Ride)
    if status:
        query = query.filter(models.Ride.status == status)
    
    # FIFO ordering for pending rides (Priority first)
    if status == models.RideStatus.PENDING:
        query = query.order_by(models.Ride.is_priority.desc(), models.Ride.created_at.asc())
    else:
        query = query.order_by(models.Ride.created_at.desc()) # Show newest completed first
        
    return query.all()

@app.post("/accept_ride/{ride_id}")
def accept_ride(ride_id: int, driver_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    if ride.status != models.RideStatus.PENDING:
        raise HTTPException(status_code=400, detail="Ride already accepted or completed")
    
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    if driver.status != models.DriverStatus.AVAILABLE:
        raise HTTPException(status_code=400, detail="Driver is busy")
    
    ride.status = models.RideStatus.ACCEPTED
    ride.driver_id = driver_id
    driver.status = models.DriverStatus.BUSY
    
    db.commit()
    return {"message": "Ride accepted"}

@app.post("/complete_ride/{ride_id}")
def complete_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    
    # Automate driver status reset
    if ride.driver_id:
        driver = db.query(models.Driver).filter(models.Driver.id == ride.driver_id).first()
        if driver:
            driver.status = models.DriverStatus.AVAILABLE
    
    ride.status = models.RideStatus.COMPLETED
    db.commit()
    return {"message": "Ride completed"}

@app.get("/drivers", response_model=List[schemas.DriverResponse])
def read_drivers(db: Session = Depends(get_db)):
    return db.query(models.Driver).all()

@app.get("/driver/{driver_id}/assigned_ride", response_model=Optional[schemas.RideResponse])
def get_assigned_ride(driver_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(
        models.Ride.driver_id == driver_id,
        models.Ride.status == models.RideStatus.ACCEPTED
    ).first()
    return ride

@app.post("/rides/{ride_id}/upgrade")
def upgrade_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    if ride.status != models.RideStatus.PENDING:
        raise HTTPException(status_code=400, detail="Can only upgrade pending rides")
    
    ride.is_priority = True
    ride.fare += 50  # Add Warp Pass fee
    db.commit()
    return {"message": "Ride upgraded to Priority"}
