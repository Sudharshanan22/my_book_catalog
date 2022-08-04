from . import auth_blueprint
from flask import render_template,request,flash,redirect,url_for
from .wtf_forms import Registration
from .models import Users


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#userlist = Users.query.all()
@auth_blueprint.route('/login',methods=["GET","POST"])
def login():
    form = Registration() #Regestiation is the form call that was created in form.property
    if request.method == "POST":
        userlist = Users.query.all()
        for username in userlist:
            if username.user_name == form.name.data and username.user_password == form.password.data:
                return render_template('signup.html',lst=form.name.data)
    return render_template('login.html',form=form)

@auth_blueprint.route('/signup',methods=["GET","POST"])
def signup():
    form = Registration() #Regestiation is the form call that was created in form.property
    if request.method == "POST":
        Users.create_user(form.name.data,form.email.data,form.password.data)
        flash("Registration sucessful...! ") ## flash messages are notifications to get (used insted of java script alert)
        return redirect(url_for("auth_blueprint.login"))
    return render_template('login.html',form=form)

@auth_blueprint.route('/logout')
def logout():
    return 'logout'
