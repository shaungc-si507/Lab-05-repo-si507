from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class University(Base):
    __tablename__ = 'university' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    id = Column(Integer, primary_key=True, autoincrement=True) # autoincrements by default
    name = Column(String(250), nullable=False) # The way we write types in SQLAlchemy is different from SQLite specifically -- and more like Python!
    capacity = Column(Integer)
    location = Column(String(250))



class College(Base):
    __tablename__ = 'college'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    capacity = Column(Integer)
    university_id = Column(Integer, ForeignKey('university.id')) # Creates a many to one relationship
    university = relationship("University") # Necessary for that relationship to be used in our code
    # When we pull this into another system, we'll use more steps. For now, this is fine.
