# app/student/forms.py

from wtforms.ext.sqlalchemy.fields import QuerySelectField

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, DateField, TextAreaField, IntegerField, validators
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, Comment, User  
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images, videos, documents

class FinprojForm(FlaskForm):
    """
    Form for student to add or edit a final year project
    """
    name = StringField('Title', validators=[DataRequired()])
    details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    category = QuerySelectField(query_factory=lambda: Category.query.all(),
                            get_label="name")
    budget = StringField('Budget')
    details = TextAreaField('Details', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
    deadline = DateField('Deadline', format='%m/%d/%Y', validators=(validators.Optional(),))
    submit = SubmitField('Submit')
    
class InternForm(FlaskForm):
	"""
	Form for student to apply for internship
	"""
		
	submit = SubmitField('Apply')
	
class CommentForm(FlaskForm):
	"""
	Form for student to add a comment
	"""
	comment = TextAreaField('Comment', render_kw={"rows":10, "cols":11}, validators=[DataRequired()])
	submit = SubmitField('Submit')

	
class VoteForm(FlaskForm):
	"""
	Form student to vote a project
	"""
	submit = SubmitField('vote')

