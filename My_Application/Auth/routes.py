from . import auth_blueprint
from flask import render_template,request,flash,redirect,url_for
from .wtf_forms import Registration
from .models import Users
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#userlist = Users.query.all()
@auth_blueprint.route('/',methods=["GET","POST"])
def login():
    form = Registration() #Regestiation is the form call that was created in form.property
    loginstatus = False
    if request.method == "POST":
        ##Checking the enterend username and password with the username and password from db
        userlist = Users.query.all()
        for username in userlist:
            if username.user_name == form.name.data and username.user_password == form.password.data:
                loginstatus = True
                #return render_template('testlogin.html',loginstatus=loginstatus,username=username.user_name,)
                return redirect(url_for("myblueprint.homepage"))
    return render_template('login.html',form=form,loginstatus=loginstatus)


@auth_blueprint.route('/signup',methods=["GET","POST"])
def signup():
    form = Registration() #Regestiation is the form call that was created in form.property
    if request.method == "POST":
        Users.create_user(form.name.data,form.email.data,form.password.data)
        flash("Registration sucessful...! ") ## flash messages are notifications to get (used insted of java script alert)
        return redirect(url_for("auth_blueprint.login"))
    return render_template('signup.html',form=form,loginstatus = False)
