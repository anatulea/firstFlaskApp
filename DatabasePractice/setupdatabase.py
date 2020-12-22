from basic import db, Puppy

# creates all the tables
db.create_all()

sam = Puppy("SAMMY", 3)
frank = Puppy("Frank", 4)


# both will print none because we  did not add puppies to  db yet
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()

print(sam.id) #1
print(frank.id) #2