#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from os import getenv

storage_var = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_var == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
