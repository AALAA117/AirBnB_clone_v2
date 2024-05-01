#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
storage_var = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
    if storage_var != "db":
        name = ""

        @property
        def cities(self):
            """
            getter attribute cities that returns
            the list of City instances
            """
            from models import storage
            cities_list = []
            for obj_city in storage.all(City).values:
                if self.id == obj_city.state_id:
                    cities_list.append(obj)
                    return (cities_list)
