from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from .models import Book

class AddBook(FlaskForm):
    title= StringField(50)
    author= StringField(50)
    avg_ratting=IntegerField()
    format=StringField(10)
    image= StringField(10)
    num_pages = IntegerField()
    pub_id=IntegerField()
    submit = SubmitField()

class UpdateBook(FlaskForm):
    avg_ratting=IntegerField()
    format=StringField(10)
    image= StringField(10)
    num_pages = IntegerField()
