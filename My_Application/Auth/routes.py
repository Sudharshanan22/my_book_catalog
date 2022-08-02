from . import auth_blueprint
from flask import render_template,request
from .wtf_forms import Registration
#from flask_restful import Api,Resource,reqparse

@auth_blueprint.route('/login',methods=["GET","POST"])
def login():
    name = None
    email = None
    form = Registration()
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
    return render_template('login.html',form=form,name=name,email=email)
@auth_blueprint.route('/signup')
def signup():
    return 'signup'
@auth_blueprint.route('/logout')
def logout():
    return 'logout'
