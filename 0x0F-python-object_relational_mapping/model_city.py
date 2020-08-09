#!/usr/bin/python3
"""
Module - Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """Links to the MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)

    # keep this order
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
