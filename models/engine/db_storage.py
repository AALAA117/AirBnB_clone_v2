#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv

user = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
database = getenv("HBNB_MYSQL_DB")
env = getenv("HBNB_ENV")


class DBStorage:
    """database storage using sqlalchemy"""
    __engine = None
    __session = None
    class_s = {
            "State": State, "City": City,
            }

    def __init__(self):
        """create engine and link it to MYSQL"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
            """query on the current database session"""
            dict_a = {}
            if cls is None:
                for item in DBStorage.class_s.values():
                    q = self.__session.query(item).all()
                    for obj in q:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        dict_a[key] = obj
            else:
                q = self.__session.query(cls).all()
                for obj in q:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dict_a[key] = obj
            return(dict_a)

    def new(self, obj):
            """add the object to the current database session"""
            if obj:
                self.__session.add(obj)

    def save(self):
            """commit all changes of the current database session"""
            self.__session.commit()

    def delete(self, obj=None):
            """delete from the current database session"""
            if obj:
                self.__session.delet(obj)

    def reload(self):
            """create all tables in the database"""
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
