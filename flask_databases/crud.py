from Models import db, Kitten

# Create

my_kitten = Kitten('Michi')
db.session.add(my_kitten)
db.session.commit()

# Read

all_kittens = Kitten.query.all() # get all the kittens in the tables
print(all_kittens)
#select by idih
Kitten_one = Kitten.query.get(1)
print(Kitten_one)

#Filters
# get all the kittens with name='michi'
kitten_michi = Kitten.query.filter_by(name='Michi')
print(kitten_michi)

#Update
first_kitten = Kitten.query.get(1)
first_kitten.name = 'Michi2'
db.session.add(first_kitten)
db.session.commit()

#Delete

second_kitten = Kitten.query.get(2)
db.session.delete(second_kitten)
db.session.commit()


all_kittens = Kitten.query.all() # get all the kittens in the tables
print(all_kittens)
