from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from . import Auth,Catalog_App

db = SQLAlchemy() #mentionaing the DB as SQLAlchemy


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
