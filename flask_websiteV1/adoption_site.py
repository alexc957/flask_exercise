from flask import Flask, render_template, url_for, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

# sql db section
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app,db)

# models

class Kitten(db.Model):
    __tablename__ = 'kitten'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Kitten name: {self.name} "

### View Functions

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add',methods=['GET','POST'])
def add_kitten():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_kitten = Kitten(name)
        db.session.add(new_kitten)
        db.session.commit()
        return redirect(url_for('list_kitten'))
    return render_template('add.html',form=form)


@app.route('/list')
def list_kitten():
    kittens = Kitten.query.all()
    return render_template('list.html',kittens=kittens)

@app.route('/delete',methods=['GET','POST'])
def del_kitten():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        kitten = Kitten.query.get(id)
        db.session.delete(kitten)
        db.session.commit()
        return redirect(url_for('list_kitten'))
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
