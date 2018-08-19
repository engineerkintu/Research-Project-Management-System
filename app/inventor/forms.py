# app/inventor/forms.py

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, DateField, TextAreaField, IntegerField, validators, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, Comment, User 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import videos, documents, images

class CategoryForm(FlaskForm):
    """
    Form for inventor to add a category
    """
    name = StringField('Name', validators=[DataRequired()])
    details = TextAreaField('Description', render_kw={"rows":5, "cols":8}, validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    """
    Form for inventor to add or edit a project
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', render_kw={"rows":6, "cols":8}, validators=[DataRequired()])
    instructions = TextAreaField('Instructions', render_kw={"rows":6, "cols":8})
    architecture = TextAreaField('Architecture', render_kw={"rows":6, "cols":8})
    components = TextAreaField('Components', render_kw={"rows":6, "cols":8})
    assembly = TextAreaField('Assembly', render_kw={"rows":6, "cols":8})
    concept = TextAreaField('Concept', render_kw={"rows":6, "cols":8})
    category = QuerySelectField(query_factory=lambda: Category.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')
    

class ResearchForm(FlaskForm): 
    """
    Form for inventor to add or edit a research
    """
    name = StringField('Title', validators=[DataRequired()])
    details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    category = QuerySelectField(query_factory=lambda: Category.query.all(), get_label="name")
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    """
    Form for inventor to add comment
    """
    message = TextAreaField('Message', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])   
    submit = SubmitField('Submit')
    
    

class ProjtitleForm(FlaskForm):
	name = StringField('Title')
	details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
	category =  QuerySelectField(query_factory=lambda: Category.query.all(), get_label="name") 
	submit = SubmitField('Submit')  

    
class DoprojForm(FlaskForm):
    """
    Form for inventor to add or edit a doproj
    """
    name = StringField('Name', validators=[DataRequired()])
    details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    budget = StringField('Budget')
    duration = StringField('Estimated Duration') 
    submit = SubmitField('Submit')
    

