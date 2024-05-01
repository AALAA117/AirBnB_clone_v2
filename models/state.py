#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
    
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
