from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "Get the hell out of here"
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    usrname = request.form.get("username")
    print("the name-" + usrname)
    email = request.form.get("email")
    print("email-" + email)
    password1 = request.form.get("password1")
    print("the password is-" + password1)
    password2 = request.form.get("password2")
    print("the password is-" + password2)


    if len(email) < 4:
        flash('Your email is short', category='!')
    elif len(password1) < 8:
        flash('Your password is less than 8 characters', category='!')
    
    elif len(usrname) < 3:
        flash('Your name should be more than 3 characters', category='!') 
    else:
        flash('Success :)') 





    return render_template("signup.html")

