from flask import Flask
from My_Application import create_app,db




if __name__ == '__main__':
    myflaskapp = create_app('dev')
    with myflaskapp.app_context():
        db.create_all()
    myflaskapp.run()
