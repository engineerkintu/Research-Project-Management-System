# app/admin/forms.py


from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField
from wtforms import StringField, SubmitField, TextField, DateField, TextAreaField, IntegerField, validators
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, User, Internship, Stock 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images, videos, documents
#from flask_bootstrap import Bootstrap
#from flask_admin.widgets import DatePickerWidget



class InternshipForm(FlaskForm):
    """
    Form for admin to add internship placements
    """
    name = StringField('Name', validators=[DataRequired()])
    details = TextAreaField('Description', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    objectives = TextAreaField('Objectives', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    requirements = TextAreaField('Requirements', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    outcomes = TextAreaField('Out comes', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    duration = StringField('Duration')
    #start_date = DateField('Deadline', wifget=DatePickerWidget())
    submit = SubmitField('Submit')
    
    
class StockForm(FlaskForm):
    """
    Form for admin to add stock of items
    """
    name = StringField('Name', validators=[DataRequired()])
    details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    purpose = TextAreaField('Purpose', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    unit_price = IntegerField('Unit price')
    img = FileField('Item image', validators=[FileAllowed(images, 'Images only!')])
    submit = SubmitField('Submit')
    
class UserForm(FlaskForm):
	"""
	Form for admin to block user
	"""
	block = QuerySelectField('Block', choices=[('active','Active'),('blocked','Block')])
	submit = SubmitField('Submit')
    
