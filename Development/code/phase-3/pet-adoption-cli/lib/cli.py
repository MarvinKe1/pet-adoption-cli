import click
from .database import SessionLocal
from . import crud

@click.group()
def cli():
    """Pet Adoption CLI"""

@cli.group()
def shelter():
    """Manage shelters"""

@shelter.command()
@click.option("--name", prompt="Shelter name")
@click.option("--location", prompt="Location")
def add(name, location):
    """Add a new shelter"""
    db = SessionLocal()
    shelter = crud.create_shelter(db, name=name, location=location)
    click.echo(f"Added shelter: {shelter.name} (ID: {shelter.id})")
    db.close()

@shelter.command()
@click.option("--id", type=int, prompt="Shelter ID")
def get(id):
    """Get shelter details"""
    db = SessionLocal()
    shelter = crud.get_shelter(db, id)
    if shelter:
        click.echo(f"Shelter {shelter.id}: {shelter.name} ({shelter.location})")
    else:
        click.echo("Shelter not found!")
    db.close()

@shelter.command()
def list():
    """List all shelters"""
    db = SessionLocal()
    shelters = crud.get_shelters(db)
    for shelter in shelters:
        click.echo(f"ID: {shelter.id}, Name: {shelter.name}, Location: {shelter.location}")
    db.close()

@cli.group()
def pet():
    """Manage pets"""

@pet.command()
@click.option("--name", prompt="Pet name")
@click.option("--species", prompt="Species")
@click.option("--shelter-id", type=int, prompt="Shelter ID")
def add(name, species, shelter_id):
    """Add a new pet"""
    db = SessionLocal()
    pet = crud.create_pet(db, name=name, species=species, shelter_id=shelter_id)
    click.echo(f"Added pet: {pet.name} (ID: {pet.id})")
    db.close()

@pet.command()
@click.option("--id", type=int, prompt="Pet ID")
def adopt(id):
    """Mark pet as adopted"""
    db = SessionLocal()
    if crud.adopt_pet(db, id):
        click.echo("Pet adopted successfully!")
    else:
        click.echo("Pet not found!")
    db.close()

@pet.command()
def list():
    """List all pets"""
    db = SessionLocal()
    pets = crud.get_pets(db)
    for pet in pets:
        status = "Adopted" if pet.adopted else "Available"
        click.echo(f"ID: {pet.id}, Name: {pet.name}, Species: {pet.species}, Status: {status}, Shelter ID: {pet.shelter_id}")
    db.close()

@pet.command()
@click.option("--id", type=int, prompt="Pet ID")
def info(id):
    """Get pet details"""
    db = SessionLocal()
    pet = crud.get_pet(db, id)
    if pet:
        click.echo(f"\nPet Details:")
        click.echo(f"Name: {pet.name}")
        click.echo(f"Species: {pet.species}")
        click.echo(f"Status: {'Adopted' if pet.adopted else 'Available'}")
        click.echo(f"Shelter ID: {pet.shelter_id}\n")
    else:
        click.echo("Pet not found!")
    db.close()

@cli.group()
def adopter():
    """Manage adopters"""

@adopter.command()
@click.option("--name", prompt="Full name")
@click.option("--email", prompt="Email")
@click.option("--phone", prompt="Phone")
def add(name, email, phone):
    """Add a new adopter"""
    db = SessionLocal()
    adopter = crud.create_adopter(db, name=name, email=email, phone=phone)
    click.echo(f"Added adopter: {adopter.name} (ID: {adopter.id})")
    db.close()

@adopter.command()
def list():
    """List all adopters"""
    db = SessionLocal()
    adopters = crud.get_adopters(db)
    for adopter in adopters:
        click.echo(f"ID: {adopter.id}, Name: {adopter.name}, Email: {adopter.email}, Phone: {adopter.phone}")
    db.close()

@adopter.command()
@click.option("--id", type=int, prompt="Adopter ID")
def info(id):
    """Get adopter details"""
    db = SessionLocal()
    adopter = crud.get_adopter(db, id)
    if adopter:
        click.echo(f"\nAdopter Details:")
        click.echo(f"Name: {adopter.name}")
        click.echo(f"Email: {adopter.email}")
        click.echo(f"Phone: {adopter.phone}\n")
    else:
        click.echo("Adopter not found!")
    db.close()

if __name__ == "__main__":
    cli()