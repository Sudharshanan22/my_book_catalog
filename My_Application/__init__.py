from flask import Flask
from flask_login import LoginManager
# LoginManager === Handles the user login, logout and remenbers users session(maintainng the connection after login)
# Helps saving the active user who have logged in
# Stores the active users ID in the session (So need to load the user ID to the session for the session to remember)
import os
from flask_sqlalchemy import SQLAlchemy
from . import Auth,Catalog_App

db = SQLAlchemy() #mention the DB as SQLAlchemy
login_manager = LoginManager()
login_manager.login_view = "auth_blueprint.login" ## Letting the login manager know the function that is used for login (ie: authentication)
login_manager.session_protection = "strong"   ## Not manditory (to delete the login history so that the credentials can not be stolen). deletes all the cookes after logout


def create_app(config='dev'):
    app = Flask(__name__,static_url_path='/static')


    #joing the current dirpath and dev.py path where the configuration for dev is created and adding the configuration to app
    configuration = os.path.join(os.getcwd(),'My_Application','myconfig',config+'.py')
    app.config.from_pyfile(configuration)

    db.init_app(app) #binds db to the flask application
    from .Catalog_App import myblueprint
    from .Auth import auth_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(myblueprint)

    return app
