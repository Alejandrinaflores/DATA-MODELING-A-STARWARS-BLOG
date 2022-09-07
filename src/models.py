import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    heigth = Column(Integer)
    skin_color = Column(String(250))
    eye_color = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favorite_character = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    favorite_planet = Column(Integer, ForeignKey('planets.id'))
    Planets = relationship(Planets)
    favorite_vehicle = Column(Integer, ForeignKey('vehicles.id'))
    Vehicles = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')