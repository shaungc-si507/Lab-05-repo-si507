# insert data - cleaner
from models import *
from db import session, init_db


engine = init_db()

# Function to handle insertions without duplicates, in this case based on name
def insert_university(uni_name, capacity, location):
    # first query based on human knowledge
    uni = session.query(University).filter_by(name=uni_name).first()
    if uni: # if there IS anything that comes from filtering on that name attribute...
        print("FOUND:", uni)
        return uni # got it, great
    else:
        # create it!
        uni = University(name=uni_name,capacity=capacity,location=location)
        session.add(uni)
        session.commit()
        return uni # either way returns reference to this university in particular

# You can write similar functions for any entity, which make it easier to handle complicated situations in which you need to avoid duplicating data, rather than situations in which you populate a database all at once.


# And then run them!

# Try running this file twice. What's different from running the plain db_insertdata file?
umich = insert_university("University of Michigan",32000,"Ann Arbor, MI")
