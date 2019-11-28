from flask import render_template
from website.forms import RegistrationForm, LoginForm
from website import app, db
#from website.models import

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form=form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template("login.html", form=form)
