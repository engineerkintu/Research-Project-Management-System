from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField, IntegerField, validators
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

from ..models import User

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    number1 = StringField('Mobile Number1')
    number2 = StringField('Mobile Number2')
    country = SelectField('Country', choices=[('ug','Uganda'),('ke','Kenya'),('tz','Tanzania'),
    					 ('rd','Rwanda'),('bd','Burundi'),('ml','Malawi'),
    					 ('sd','Sudan')], validators=[DataRequired()])
    sex = SelectField('Gender', choices=[('male','Male'),('female','Female')], validators=[DataRequired()])
    user_photo = FileField('User Photo', validators=[FileAllowed(images, 'Images only!')])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
