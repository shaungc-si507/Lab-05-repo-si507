from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean # Added a bit here to create association tables...
from sqlalchemy.orm import relationship
from db import Base

# contained in variable, no meaning; first argument is a string w name meaning
enrollment_table = Table('enrollment', Base.metadata,
    Column('college_id', Integer, ForeignKey('college.id')),
    Column('student_id', Integer, ForeignKey('student.id')))

class University(Base):
    __tablename__ = 'university' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    id = Column(Integer, primary_key=True, autoincrement=True) # autoincrements by default
    name = Column(String(250), nullable=False) # The way we write types in SQLAlchemy is different from SQLite specifically -- and more like Python!
    capacity = Column(Integer)
    location = Column(String(250))
    # to be able to refer to a university's colleges directly with e.g. a colleges attribute, we have to add a little bit more code than this -- but we'll let that go for now

    def __repr__(self):
        return "{} in {}".format(self.name, self.location)


class College(Base):
    __tablename__ = 'college'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    capacity = Column(Integer)
    university_id = Column(Integer, ForeignKey('university.id')) # Creates a many to one relationship
    university = relationship("University") # Necessary for that relationship to be used in our code
    students = relationship("Student",secondary=enrollment_table,backref="colleges")

    def __repr__(self):
        return "{} - holds {} students - {}".format(self.name, self.capacity,self.university.__repr__()) # so meta

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    middle_name = Column(String(250))
    grad_status = Column(Boolean) #True if grad student, False otherwise
    def __repr__(self):
        return "{}, {} {}".format(self.lastname, self.firstname, self.middle_name)
