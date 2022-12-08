import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

SWBase = declarative_base()

class users(SWBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(280), nullable=False)
    email = Column(String(280),)
    password = Column(String(280))
    loginStatus = Column(String(280))
    admin = Column(Boolean())
    lastLogin = Column(DateTime(0))

class characters(SWBase):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(280))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(280))
    skin_color = Column(String(280))
    birth_year = Column(String(280))
    gender = Column(String(280))
    homeworld = Column(String(280), ForeignKey('planets.id'))
    films = Column(String(280), ForeignKey('films.id'))
    species = Column(String(280), ForeignKey('species.id'))
    vehicles = Column(String(280), ForeignKey('vehicles.id'))
    starships = Column(String(280), ForeignKey('starships.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))

class planets(SWBase):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(280))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(280))
    gravity = Column(String(280))
    terrain = Column(String(280))
    surface_water = Column(Integer)
    population = Column(Integer)
    residents = Column(String(280), ForeignKey('characters.id'))
    films = Column(String(280), ForeignKey('films.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))

class films(SWBase):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String(280))
    episode_id = Column(Integer)
    opening_crawl = Column(String(600))
    director = Column(String(280))
    producer = Column(String(280))
    release_date = Column(Date())
    characters = Column(String(280), ForeignKey('characters.id'))
    planets = Column(String(280), ForeignKey('planets.id'))
    starships = Column(String(280), ForeignKey('starships.id'))
    vehicles = Column(String(280), ForeignKey('vehicles.id'))
    species = Column(String(280), ForeignKey('species.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))


class species(SWBase):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String(280))
    clasification = Column(String(280))
    designation = Column(String(280))
    average_height = Column(Integer)
    skin_colors = Column(String(280))
    hair_colors = Column(String(280))
    eyes_colors = Column(String(280))
    average_lifespan = Column(Integer)
    homeworld = Column(String(280), ForeignKey('planets.id'))
    languaje = Column(String(280))
    characters = Column(String(280), ForeignKey('characters.id'))
    films = Column(String(280), ForeignKey('films.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))

class vehicles(SWBase):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(280))
    model = Column(String(280))
    manufacturer = Column(String(280))
    cost_in_credits = Column(Integer)
    length = Column(Float)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(280))
    vehicle_class = Column(String(280))
    pilots = Column(String(280), ForeignKey('characters.id'))
    films = Column(String(280), ForeignKey('films.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))

class starships(SWBase):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    name = Column(String(280))
    model = Column(String(280))
    manufacturer = Column(String(280))
    cost_in_credits = Column(Integer)
    length = Column(Float)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(280))
    hyperdrive_rating = Column(Float)
    mglt = Column(Integer)
    starship_class = Column(String(280))
    pilots = Column(String(280), ForeignKey('characters.id'))
    films = Column(String(280), ForeignKey('films.id'))
    created = Column(DateTime(0))
    edited = Column(DateTime(0))
    url = Column(String(280))

class favorites(SWBase):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    charachters_id = Column(Integer, ForeignKey('charachters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    users = relationship("user")
    favorite_charachter = relationship("characters")
    favorite_planets = relationship("planets")
    favorite_films = relationship("films")
    favorite_species = relationship("species")
    favorite_vehicles = relationship("vehicles")
    favorite_starships = relationship("starships")

    #   def to_dict(self):
    #       return {}

## Draw from SQLAlchemy base
render_er(SWBase, 'Diagram.png')