#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv
storage_var = getenv("HBNB_TYPE_STORAGE")

place_amenity = Table(
        "place_amenity", Base.metadata,
        Column('place_id', String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column('amenity_id', ForeignKey("amenities.id"),
               primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete-orphan",
                           backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             back_populates="place_amenities",
                             viewonly=False)

    if storage_var != "db":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of Review instances"""
            reviews_list = []
            from models import storage
            for obj_review in storage.all(Review).values():
                if self.id == obj_review.id:
                    reviews_list.append(obj_review)
            return (reviews_list)

        @property
        def amenities(self):
            """returns the list of Amenity instances"""
            obj_amenity = []
            for amenity_id in self.amenity_ids:
                key = "{}.{}".format("Amenity", amenity_id)
                if key in self.FileStorage.__objects:
                    obj_amenity.append(self.FileStorage.__objects[key])
            return (obj_amenity)

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding an Amenity.id"""
            try:
                if type(obj).__name__ == "Amenity":
                    if self.id == obj.id:
                        self.amenity_ids.append(obj.id)
            except Exception as err:
                pass
