#!/usr/bin/python3
'''
Script to define a City class and a base class to work with
SQLalchemy ORM
'''

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class State(Base):
    '''
    The city class

    Attributes:
        __tablename__: The table name
        id: int state id of the class
        name: The state name of the class
        state_id(int): the state the city belongs to
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
