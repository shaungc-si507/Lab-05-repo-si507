from models import College, University # Specific -- if you had a LOT you might import *
from db import session, init_db


init_db()
# This does the connection all in one step
# After we do that basic setup, it is MUCH easier/is possible to insert data using the code we've built up.


# Insert a university into the database - in the university table

# First create an instance of our model University -- almost coming full circle
new_uni = University(name='University of California - Berkeley',capacity=22000,location="Berkeley, CA")
session.add(new_uni) # A lot like the git add idea
session.commit()

new_college = College(name="iSchool",capacity=2000,university=new_uni) # It really is that easy
# Just have to be careful we're either
# -- using conditionals
# -- being really careful about what code to run + constraints in our schema
# in order to avoid tons and tons of duplicate insertions into our tables
session.add(new_college)
session.commit()
# IMPORTANT - changes you make via the SQLite DB browser don't truly take effect forever until you *save* the changes made in the browser.
# If you have the DB Browser open and connected to a database, you won't be able to run code using a db Session, because the database can only have one connection. It's like when you open a file in a program and don't close it, you can't open it again...except now everything on the computer that can access the db is playing the metaphorical game, not just one program.

# NOTE -- If we want to add a college for a university ALREADY there (say, before this program was written, which is different from that new_uni which is created IN the program) -- we have to do a query to check if it exists and then refer to that instance
# Super do-able!
# But first, let's just do this -- we'll provide additional resources that show examples like that, and may get a chance to talk about it live!



# TODO - Add more universities and colleges to the data!
# Two new universities
# One college for each!

# Think about writing the code, then run it and test it out.

# Don't worry!! if you create duplicates for now! More important to create something to add to db tables!
