from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


#from My_Application import db


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Publication name : {self.name} ({self.id})"

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    author = db.Column(db.String(50))
    avg_ratting = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100),unique=True)
    num_pages = db.Column(db.Integer)
    pub_id = db.Column(db.Integer,db.ForeignKey("publication.id"))
    def __init__(self,title,author,avg_ratting,format,image,num_pages,pub_id):
        self.title = title
        self.author = author
        self.avg_ratting = avg_ratting
        self.format = format
        self.image = image
        self.num_pages= num_pages
        self.pub_id= pub_id
    def __repr__(self):
        return f" {self.title} by {self.author}"
