from . import auth_blueprint
from flask import render_template,request,flash,redirect,url_for
from flask_login import login_user,logout_user
from .wtf_forms import Registration,loginForm
from .models import Users
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#userlist = Users.query.all()
@auth_blueprint.route('/',methods=["GET","POST"])
def login():
    form = loginForm() #Regestiation is the form call that was created in form.property
    loginstatus = False
    if request.method == "POST":
        ##Checking the enterend username and password with the username and password from db
        userentry = Users.query.filter_by(user_name=form.name.data).first()

        if not userentry or form.password.data != userentry.user_password:
            flash("Invalid credentials please try again")
            return redirect(url_for("auth_blueprint.login"))
        ## Login_user remembers that the session is logged in after login
        ## done with the imported inbuilt login_user function that takes (user object,a boolian value where True = logged in)
        #login_user(userentry,form.stay_loggedin.data)
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
