from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return "<User >"

    def serialize(self):
        return {
            "id": self.id, 
            "username": self.username, 
            "email": self.email
        }



class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), unique=True, nullable=False)

    characters = db.relationship("Character", back_populates="items")
    planets = db.relationship("Planet", back_populates="items")
    starships = db.relationship("Starship", back_populates="items")
    favourites = db.relationship("Favourite", back_populates="items")

    def __repr__(self):
        return "<Item %r>" % {self.name, self.id}

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "img": self.img,
            "description": self.description,
        }


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
    

    items = db.relationship("Item", back_populates="characters")
    def __repr__(self):
        return "<Character >"

    def serialize(self):
        return {
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            
        }


class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String, nullable=False)
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
    

    items = db.relationship("Item", back_populates="planets")

    def __repr__(self):
        return "<Planet >"

    def serialize(self):
        return {
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
           
        }


class Starship(db.Model):
    __tablename__ = "starships"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    starship_class = db.Column(db.String, nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphere_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.String, nullable=False)
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
   

    items = db.relationship("Item", back_populates="starships")

    def __repr__(self):
        return "<Starship >"

    def serialize(self):
        return {
            "model": self.model,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphere_speed": self.max_atmosphere_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
           
        }
    
class Favourite(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    items = db.relationship("Item", back_populates="favourites")

    def __repr__(self):
        return "<Favourite >"

    def serialize(self):
        return {
            "id": self.item_id,
            "name": self.items.name,
            "description": self.items.description,
            "img": self.items.img,
        }
    
engine = create_engine(
    "postgresql://gitpod:postgres@localhost:5432/example"
    ) 
db.Model.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()