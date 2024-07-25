from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
import os

@app.route("/")


@app.route("/login")
def login():
    return render_template("home.html")