from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField , URLField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import  User


class LoginForm(FlaskForm):
   email = StringField('Email' , validators=[DataRequired() , Email()])
   password = PasswordField('Password' , validators=[DataRequired()])
   rememberme = BooleanField('Remember me')
   submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
   username = StringField('Username' , validators=[DataRequired() , Length(min=2 , max=200)])
   email = StringField('Email' , validators=[DataRequired() , Email()])
   password = PasswordField('Password' , validators=[DataRequired()])
   submit = SubmitField('Register')

   def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
   def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')




