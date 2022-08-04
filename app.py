from flask import Flask
from My_Application import create_app,db,Auth
from My_Application.Auth.models import Users



if __name__ == '__main__':
    myflaskapp = create_app('dev')

    with myflaskapp.app_context():
        db.create_all()


        # if not Users.query.filter_by(user_name="kana").first():
        #      Users.create_user("kana","kanna@tcs.com","helohello")




    myflaskapp.run(debug=True)
