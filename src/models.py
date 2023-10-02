import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(20), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthyear = Column(String)
    gender = Column(String)
    height = Column(Integer)
    skin_color = Column(String)
    eye_color = Column(String)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)
    Climate = Column(String)
    Terrain = Column(String)
    Gravity = Column(String)
    Water = Column(Integer)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    vehicle_class = Column(String)
    manufacturer = Column(String)
    crew = Column(Integer)
    passengers = Column(Integer)

class FavoriteVehicle(Base):
    __tablename__ = 'favorite_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
