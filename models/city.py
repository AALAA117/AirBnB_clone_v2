#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from models.base_model import BaseModel, Base
from os import getenv

storage_var = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storage_var == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""
