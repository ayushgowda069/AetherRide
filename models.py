from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from .database import Base

class RideStatus(str, enum.Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    COMPLETED = "COMPLETED"

class DriverStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Enum(DriverStatus), default=DriverStatus.AVAILABLE)

    rides = relationship("Ride", back_populates="driver")

class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    pickup_location = Column(String)
    destination = Column(String)
    fare = Column(Integer, default=0)
    is_priority = Column(Boolean, default=False)
    status = Column(Enum(RideStatus), default=RideStatus.PENDING)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    driver = relationship("Driver", back_populates="rides")
