from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .models import RideStatus, DriverStatus

class RideBase(BaseModel):
    user_name: str
    pickup_location: str
    destination: str

class RideCreate(RideBase):
    fare: int = 0
    is_priority: bool = False

class RideResponse(RideBase):
    id: int
    fare: int
    is_priority: bool
    status: RideStatus
    driver_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

class DriverBase(BaseModel):
    name: str

class DriverResponse(DriverBase):
    id: int
    status: DriverStatus

    class Config:
        orm_mode = True
