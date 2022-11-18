#!/usr/bin/python3
"""This module that contains the class definition of a State
    and an instance Base = declarative_base().
   Created on Sunday, December 13, 2022
   @author: DaisyG Chipana Lapa
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Declare Class Base that inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)