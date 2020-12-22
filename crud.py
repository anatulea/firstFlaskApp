# CREATE ENTRIES INTO TABLE
from models import db, Puppy, Owner, Toy

# CREATE 2 PUPPIES

rufus = Puppy("Rufus")
fido = Puppy("Fido")
db.session.add_all([rufus, fido])
db.session.commit()
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

jose = Owner('Jose', rufus.id)
# give rufus toys
toy_one = Toy("Chew Toy", rufus.id)
toy_two = Toy('Ball', rufus.id)

db.session.add_all([jose, toy_one, toy_two])
db.session.commit()

rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

print(rufus.report_toys())