from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
from application.form import LoginForm , RegistrationForm , FacilitiesForm
from flask_login import current_user , login_user , logout_user , login_required
from application.models import User , Facilities
import os

@app.route("/" , methods = ['POST' , 'GET'])
def index():

    if current_user.is_authenticated:
        return redirect(url_for('home'))


    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successful!')
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember = form.remember.data)
            return redirect(url_for('home'))
    return render_template("login.html" , form = form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup" , methods = ['POST' , 'GET'])
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('index'))
    return render_template('signup.html' , form = form)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/facilitiesform' , methods = ['POST' , 'GET'])
def facilitiesform():
    form = FacilitiesForm()
    if form.validate_on_submit():
       facilities = Facilities(message = form.message.data , author = current_user)
       db.session.add(facilities)
       db.session.commit()
       flash(f'Message is sent!')
       return redirect(url_for('facilitiesform'))
    return render_template('facilitiesform.html' , form = form)


@app.route('/mycomplaints')
def mycomplaints():
    facilities = Facilities.query.all()
    return render_template('mycomplaints.html' , facilities = facilities)




