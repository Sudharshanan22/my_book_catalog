from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from .models import Users


## Crearing a custom validadtor to check if the email already exist
def EmailExistValidator(form,field):
    email_check = User.query.filter_by(user_email = "field.data").first()
    if email_check:
        raise ValidationError("Email already exist")

class Registration(FlaskForm):
    name = StringField("Your Name",validators=[DataRequired(),Length(4,20)])
    email = EmailField("E-mail Address",validators=[DataRequired(),EmailExistValidator])
    password = PasswordField("Password",validators=[DataRequired(),Length(5),EqualTo('confirm',message='Password must match')])
    confirm = PasswordField("Conferm password",validators=[DataRequired(),Length(5),EqualTo('password',message='Password must match')])
    submit = SubmitField()

class loginForm(FlaskForm):
    name = StringField("Your Name",validators=[DataRequired(),Length(4,20)])
    password = PasswordField("Password",validators=[DataRequired(),Length(5)])
    stay_loggedin = BooleanField("stay logged-in")
    submit = SubmitField()
