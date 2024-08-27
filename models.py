from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, Date, DateTime, Float, PickleType
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from database import Base
from sqlalchemy.ext.mutable import MutableDict


class Attraction(Base):
    __tablename__ = "attractions"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column(String(2000))
    address = Column(String(300))
    coordinate_x = Column(Float)
    coordinate_y = Column(Float)
    region_id = Column(Integer, ForeignKey("regions.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    region = relationship("Region", back_populates="attractions", foreign_keys=[region_id])
    category = relationship("Category", back_populates="attractions", foreign_keys=[category_id])


    def __init__(self, name, description, address, coordinate_x, coordinate_y):
        self.name = name
        self.description = description
        self.address = address
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))

    attractions = relationship("Attraction", back_populates="region")

    def __init__(self, name):
        self.name = name


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))

    attractions = relationship("Attraction", back_populates="category")

    def __init__(self, name):
        self.name = name

