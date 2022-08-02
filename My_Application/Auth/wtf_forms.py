from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField

class Registration(FlaskForm):
    name = StringField()
    email = EmailField()
    submit = SubmitField()
