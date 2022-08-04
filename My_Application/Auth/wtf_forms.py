from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError


class Registration(FlaskForm):
    name = StringField("Your Name",validators=[DataRequired(),Length(4,20)])
    email = EmailField("E-mail Address",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),Length(5),EqualTo('confirm',message='Password must match')])
    confirm = PasswordField("Conferm password",validators=[DataRequired(),Length(5),EqualTo('password',message='Password must match')])
    submit = SubmitField()
