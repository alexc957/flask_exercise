from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekyegoeshere'

class InfoForm(FlaskForm):
    kitten_name = StringField("What is your Name?")
    submit = SubmitField()
"""
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/info')
def info():
    return "<h1> Kittens are cute!</h1>"
#dynamic route

@app.route('/kitten/<name>')
def kitten(name):
    #return '<h1> this is a page for {} </h1>'.format(name)
    return render_template('kitten.html',name=name)
"""

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')
@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html',first=first,last=last)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/info_form',methods=['GET','POST'])
def info_form():
    name  = False
    form = InfoForm()
    if form.validate_on_submit():
        name = form.kitten_name.data
        form.kitten_name.data = ''
    return render_template('info_form.html',name=name,form=form)
if __name__ == '__main__':
    app.run(debug=True)
