from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
from application.form import LoginForm
import os

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login")
def login():
    form = LoginForm()

    if form.validate_on_submit():
       

       return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")




