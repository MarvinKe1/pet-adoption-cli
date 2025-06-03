from lib.database import SessionLocal, engine
from lib.models import Base
from lib import crud, models
import random

def generate_phone():
    return f"+2547{random.randint(10, 99)}{random.randint(100000, 999999)}"

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Clear existing data first to avoid duplicates
        db.query(models.Pet).delete()
        db.query(models.Adopter).delete()
        db.query(models.Shelter).delete()
        db.commit()

        # Shelters
        shelters = [
            crud.create_shelter(db, name="Paws Haven", location="Nairobi"),
            crud.create_shelter(db, name="Whisker Rescue", location="Mombasa"),
            crud.create_shelter(db, name="Animal Friends", location="Kisumu")
        ]

        # Pets
        pets = [
            crud.create_pet(db, name="Buddy", species="Dog", shelter_id=1),
            crud.create_pet(db, name="Luna", species="Cat", shelter_id=2),
            crud.create_pet(db, name="Max", species="Dog", shelter_id=1),
            crud.create_pet(db, name="Bella", species="Rabbit", shelter_id=3)
        ]

        # Adopters
        adopters = [
            crud.create_adopter(db, name="Zawadi Muthoni", email="zawadi@example.com", phone=generate_phone()),
            crud.create_adopter(db, name="Alice Johnson", email="alice@example.com", phone=generate_phone()),
            crud.create_adopter(db, name="Brian Smith", email="brian@example.com", phone=generate_phone())
        ]

        # Adopt a pet
        crud.adopt_pet(db, pet_id=1)
        
        db.commit()

        # Print results
        print("Database seeded successfully!")
        print(f"Shelters: {', '.join([s.name for s in shelters])}")
        print(f"Pets: {', '.join([p.name for p in pets])}")
        print(f"Adopters: {', '.join([a.name for a in adopters])}")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()