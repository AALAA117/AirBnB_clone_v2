#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Integer, String, Column, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
storage_var = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True, default="NULL")
    last_name = Column(String(128), nullable=True, default="NULL")
    places = relationship("Place", cascade="all, delete-orphan", backref="user")
    reviews = relationship("Review", cascade="all, delete-orphan", backref="user")
    if storage_var != "db":
        email = ""
        password = ""
        first_name = ""
        last_name = ""
