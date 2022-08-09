from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    user_name = db.Column(db.String(50), nullable = False)
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50),nullable = False)

    @classmethod
    def create_user(cls,user,email,password):
        user = cls(user_name=user, user_email=email, user_password=password)
        db.session.add(user)
        db.session.commit()
        return user
