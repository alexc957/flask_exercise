from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of the kittne')
    submit = SubmitField('Add Kitten')

class DelForm(FlaskForm):
    id = IntegerField("Id number of kitten to be remove ")
    submit = SubmitField("Remove")
