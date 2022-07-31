from . import auth_blueprint
from flask import render_template
@auth_blueprint.route('/login')
def login():
    return render_template('login.html')
@auth_blueprint.route('/signup')
def signup():
    return 'signup'
@auth_blueprint.route('/logout')
def logout():
    return 'logout'
