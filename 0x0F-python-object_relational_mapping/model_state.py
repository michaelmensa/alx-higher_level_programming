#!/usr/bin/python3
'''
Script to define a State class and a base class to work with
SQLalchemy ORM
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    The state class

    Attributes:
        __tablename__: The table name
        id: int state id of the class
        name: The state name of the class
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
