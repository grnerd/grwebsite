from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/root")
def root():
    return render_template("root.html")
@views.route("/login")
def login():
    return render_template("login.html")
@views.route("/sign-up")
def sing_up():
    return render_template("signup.html")       
@views.route("/gr")
def google_login():
    return render_template("glogin.html")