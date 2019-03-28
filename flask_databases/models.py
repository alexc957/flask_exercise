import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
#\__file__ = models.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
Migrate(app,db) #connects the application to the database
class Kitten(db.Model):
    # override the table name
    __tablename__ = 'kitten'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # one kitten can have many toys
    toys = db.relationship('Toy',backref='kitten',lazy='dynamic')
    # one to one: one kitten have one owner
    owner = db.relationship('Owner',backref='kitten',uselist=False)




    def __init__(self,name):
        self.name = name


    def __repr__(self):
        if self.owner:
            return f" kitten name: {self.name} and owner: {self.owner.name} "
        return f"kitten name: {self.name}  and has no owner yet"

    def report_toys(self):
        print("here my toys")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tablename__='toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    kitten_id = db.Column(db.Integer,db.ForeignKey('kitten.id'))

    def __init__(self,item_name,kitten_id):
        self.item_name = item_name
        self.kitten_id = kitten_id


class Owner(db.Model):
    __tablename__='owners'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    kitten_id = db.Column(db.Integer,db.ForeignKey('kitten.id'))

    def __init__(self,name,kitten_id):
        self.name = name
        self.kitten_id = kitten_id
