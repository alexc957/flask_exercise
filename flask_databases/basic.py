from models import db, Kitten,Owner, Toy


# craate two kittens
michi = Kitten('Michi')
pancho = Kitten('Pancho')
db.session.add_all([michi,pancho])
db.session.commit()

# check

print(Kitten.query.all())

michi = Kitten.query.filter_by(name='Michi').first()
print(michi)
# create a owner

alex = Owner('Alex',michi.id)

#give michi some toys
toy1 = Toy('Chew toy',michi.id)
toy2 = Toy('Ball',michi.id)

db.session.add_all([alex,toy1,toy2])
db.session.commit()

michi = Kitten.query.filter_by(name='Michi').first()
print(michi)
michi.report_toys() 
