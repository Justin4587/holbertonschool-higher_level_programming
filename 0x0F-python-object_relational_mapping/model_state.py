#!/usr/bin/python3
""" I'm going to be mad """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ I'm nervous about not having a doc string """

    __tablename__ = 'states'

    id = Column(Integer, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
