from models import College, University
from db import session, init_db


engine = init_db()
# Again -- all the boilerplate that has to go together to rely on the session for doing easy insertions/queries in Python. We need access to an engine now, so we'll capture the return val from init_db.


# Now let's write some code to do some queries
# Wouldn't always just do this in a script -- might do it... in a separate application and simply write code to create and populate the db, for example!
# But let's try to see how it will work, because we'll rely on this type of structure for more stuff later.


# If only use SQL select statement without ORM...
connection = engine.connect()
result = connection.execute("select * from University")
for row in result:
    print(*row)
connection.close()


# Almost there but not quite
#session.query(University) # Doesn't get us anywhere that useful if we run this line -- it's just a query object this evaluates to! No data we can see, not stored anywhere in the *program*...

# Actually query for all the universities in the database
all_unis = session.query(University).all() # That last method *gets* -- and returns -- something that acts a lot like a list...
print(all_unis) # Let's see it

# Just the first university in the database
first_uni = session.query(University).first()
print(first_uni) # Let's see it

# Wait... this is no good, they don't look like anything!!!

# Can we print out any data values?

for u in all_unis:
    print(u.name)
    print("^ is at", u.location)

# Great!

# TODO: How can we fix this problem of not being able to print out an individual instance of one university?
# HINT: We've seen a similar problem when we started dealing with OOP... and now we know about more special methods...
# HINT: Maybe we can fix this in the *models* code itself!
# HINT: What if there were a method in the model class to represent something...

# We've already got code to add data to the database, so it's OK (for now) if we just delete the database and all its data, right? Let's fix the model and do it all again so we've definitely got a good setup.
