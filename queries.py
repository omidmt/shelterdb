import datetime
from sqlalchemy.orm import *
from sqlalchemy.sql.functions import func

import database_setup as ds
from database_setup import Base, Puppy, Shelter

engine = ds.engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_1():
    """all of the puppies and return the results in ascending alphabetical order
    """
    puppies = session.query(Puppy.name).order_by(Puppy.name.asc()).all()
    for name in puppies:
        print name[0]

def query_2():
    """all of the puppies that are less than 6 months old organized by the youngest first
    """
    six_month_ago = datetime.date.today() - datetime.timedelta(days=182)

    puppies = session.query(Puppy).filter(Puppy.dateOfBirth >= six_month_ago).order_by(Puppy.dateOfBirth.desc()).all()
    for p in puppies:
        print p.name, p.dateOfBirth

def query_3():
    """all puppies by ascending weight
    """
    puppies = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
    for p in puppies:
        print p[0], p[1]


def query_4():
    """all puppies grouped by the shelter in which they are staying
    """
    puppies = session.query(Shelter.name, func.count(Puppy.id)).join(Puppy).group_by(Puppy.shelter_id)
    # print puppies
    for p in puppies:
        print p[0], p[1]

query_4()
