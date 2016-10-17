import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()

# Shelter domain
class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(300), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    zipCode = Column(String(20), nullable=True)
    website = Column(String(150), nullable=True)


# Puppy domain
class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    dateOfBirth = Column(Date, nullable=True)
    gender = Column(String(10), nullable=False)
    weight = Column(Float, nullable=True)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    picture = Column(String(200))



# Engine and connection
engine =  create_engine('sqlite:///shelter.db')
Base.metadata.create_all(engine)