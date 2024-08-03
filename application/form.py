from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField , URLField , SelectField 
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import  User


class LoginForm(FlaskForm):
   email = StringField('Email' , validators=[DataRequired() , Email()])
   password = PasswordField('Password' , validators=[DataRequired()])
   remember = BooleanField('Remember me')
   submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
   username = StringField('Username' , validators=[DataRequired() , Length(min=2 , max=200)])
   email = StringField('Email' , validators=[DataRequired() , Email()])
   password = PasswordField('Password' , validators=[DataRequired()])
   confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password')])
   submit = SubmitField('Register')

   def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
   def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')
        

class FacilitiesForm(FlaskForm):
    hostelblock = SelectField('Hostel Block' , choices=[('ALPHA' , 'ALPHA') , ('BETA' , 'BETA') , ('GAMMA' , 'GAMMA') , ('SIGMA' , 'SIGMA')] , validators=[DataRequired()])
    hostelparts = SelectField('Hostel Parts' , choices =[('A' , 'A') , ('B' , 'B') , ('C','C') , ('D' , 'D')] , validators=[DataRequired()])
    hostelroom = StringField('Hostel Room' , validators=[DataRequired()])
    message = StringField('Messsage' , validators=[DataRequired()])
    photo_evidence = FileField('Image' , validators=[FileAllowed(['jpg' , 'png' , 'jpeg'] , 'Only images in jpg , png or jpeg are allowed!')])
    submit = SubmitField('Submit')



class IntegrityForm(FlaskForm):
    hostelblock = SelectField('Hostel Block' , choices=[('ALPHA' , 'ALPHA') , ('BETA' , 'BETA') , ('GAMMA' , 'GAMMA') , ('SIGMA' , 'SIGMA')] , validators=[DataRequired()])
    hostelparts = SelectField('Hostel Parts' , choices =[('A' , 'A') , ('B' , 'B') , ('C','C') , ('D' , 'D')] , validators=[DataRequired()])
    hostelroom = StringField('Hostel Room' , validators=[DataRequired()])
    message = StringField('Messsage' , validators=[DataRequired()])
    photo_evidence = FileField('Image' , validators=[FileAllowed(['jpg' , 'png' , 'jpeg'] , 'Only images in jpg , png or jpeg are allowed!')])
    submit = SubmitField('Submit')




    




