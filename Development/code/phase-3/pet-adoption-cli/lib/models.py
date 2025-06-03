from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Shelter(Base):
    __tablename__ = "shelters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    location = Column(String)
    pets = relationship("Pet", back_populates="shelter")

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)
    adopted = Column(Boolean, default=False)
    shelter_id = Column(Integer, ForeignKey("shelters.id"))
    shelter = relationship("Shelter", back_populates="pets")

class Adopter(Base):
    __tablename__ = "adopters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)