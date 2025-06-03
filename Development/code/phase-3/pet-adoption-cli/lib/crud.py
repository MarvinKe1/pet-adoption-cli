from sqlalchemy.orm import Session
from . import models

# Shelter operations (4)
def create_shelter(db: Session, name: str, location: str):
    db_shelter = models.Shelter(name=name, location=location)
    db.add(db_shelter)
    db.commit()
    db.refresh(db_shelter)
    return db_shelter

def get_shelter(db: Session, shelter_id: int):
    return db.query(models.Shelter).filter(models.Shelter.id == shelter_id).first()

def get_shelters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shelter).offset(skip).limit(limit).all()

def update_shelter(db: Session, shelter_id: int, name: str = None, location: str = None):
    shelter = db.query(models.Shelter).filter(models.Shelter.id == shelter_id).first()
    if not shelter:
        return None
    if name:
        shelter.name = name
    if location:
        shelter.location = location
    db.commit()
    db.refresh(shelter)
    return shelter

# Pet operations (6)
def create_pet(db: Session, name: str, species: str, shelter_id: int):
    db_pet = models.Pet(name=name, species=species, shelter_id=shelter_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100, adopted: bool = None):
    query = db.query(models.Pet)
    if adopted is not None:
        query = query.filter(models.Pet.adopted == adopted)
    return query.offset(skip).limit(limit).all()

def update_pet(db: Session, pet_id: int, name: str = None, species: str = None):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        return None
    if name:
        pet.name = name
    if species:
        pet.species = species
    db.commit()
    db.refresh(pet)
    return pet

def adopt_pet(db: Session, pet_id: int):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        return False
    pet.adopted = True
    db.commit()
    return True

def delete_pet(db: Session, pet_id: int):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        return False
    db.delete(pet)
    db.commit()
    return True

# Adopter operations (5)
def create_adopter(db: Session, name: str, email: str, phone: str):
    db_adopter = models.Adopter(name=name, email=email, phone=phone)
    db.add(db_adopter)
    db.commit()
    db.refresh(db_adopter)
    return db_adopter

def get_adopter(db: Session, adopter_id: int):
    return db.query(models.Adopter).filter(models.Adopter.id == adopter_id).first()

def get_adopters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Adopter).offset(skip).limit(limit).all()

def update_adopter(db: Session, adopter_id: int, name: str = None, email: str = None, phone: str = None):
    adopter = db.query(models.Adopter).filter(models.Adopter.id == adopter_id).first()
    if not adopter:
        return None
    if name:
        adopter.name = name
    if email:
        adopter.email = email
    if phone:
        adopter.phone = phone
    db.commit()
    db.refresh(adopter)
    return adopter

def delete_adopter(db: Session, adopter_id: int):
    adopter = db.query(models.Adopter).filter(models.Adopter.id == adopter_id).first()
    if not adopter:
        return False
    db.delete(adopter)
    db.commit()
    return True