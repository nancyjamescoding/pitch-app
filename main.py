import logging
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from configs.base_config import *
from app.templates import LogInForms, SignupForm

# creating an instance of my app.
app = Flask(__name__)
# specify db enviroment
app.config.from_object(Development)
# create my sqlalchemy instance
db = SQLAlchemy(app)

# application endpoint.


@app.route("/")
def home():
    return render_template("index.html")

# login


@app.route('/login')
def login():
    form = LogInForms
    return render_template("login.html", form=form)
# signup


@app.route('/signup')
def signup():
    form = SignupForm()
    return render_template("signup.html", form=form)
# logout


@app.route('/logout')
def logout():
    return "logout Endpoint"


if __name__ == '__main__':
    app.run(debug=True)
