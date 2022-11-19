#!/usr/bin/python3
"""This module that contains the class definition of a City
    and an instance Base = declarative_base()
    Created on Nov 17 09:33:11 2022
    @author: Avelino Carvajal
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """ Declare Class Base that inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
