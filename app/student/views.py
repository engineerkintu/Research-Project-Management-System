# app/student/views.py


from flask import abort, flash, redirect, render_template, url_for, request, make_response, Response, redirect, json, jsonify, session
from flask_login import current_user, login_required

from . import student
from ..student.forms import FinprojForm, InternForm, CommentForm, VoteForm
from .. import db
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, Internship, Intern, Comment, Vote


import datetime

def check_student():
    """
    Prevent non-students from accessing the page
    """
    if not current_user.is_student:
        abort(403)

# Final Year Project Views

@student.route('student/studentprojects', methods=['GET', 'POST'])
@login_required
def list_finprojs():
    """
    List all projects
    """
    check_student()

    finprojs = Finproj.query.all()

    return render_template('student/finprojs/finprojs.html',
                           finprojs=finprojs, title="Projects and Assignments")

@student.route('student/finprojs/add', methods=['GET', 'POST'])
@login_required
def add_finproj():
    """
    Add a final year project to the database
    """
    check_student()

    add_finproj = True

    form = FinprojForm()
    if form.validate_on_submit():  	
    	user = current_user.id
    	finproj = Finproj(name=form.name.data,
    	                  category = form.category.data,
    	                  user_id = user,
    	                  details = form.details.data,
    	                  budget = form.budget.data,
    	                  deadline = datetime.datetime.utcnow(),
    	                  date = datetime.datetime.utcnow()
    	                  )
    	
    	try:
    		# add final year project to the database
    		db.session.add(finproj)
    		db.session.commit()
    		flash('You have successfully added a new project/ assignement.')
    	except:
    		# in case project name already exists
    		flash('Error: project name already exists.')
    		
    	# redirect to projects page
    	return redirect(url_for('student.list_finprojs'))

    # load projects template
    return render_template('student/finprojs/finproj.html', action="Add",
                           add_finproj=add_finproj, form=form,
                           title="Add Project or Assignment")
    	

@student.route('/student/finprojs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_finproj(id):
    """
    Edit a project
    """
    check_student()

    add_finproj = False

    finproj = Finproj.query.get_or_404(id)
    form = FinprojForm(obj=finproj)
    user = current_user.id
    if form.validate_on_submit():
    	finproj.name = form.name.data
    	finproj.details = form.details.data
    	finproj.category = form.category.data
    	finproj.budget = form.budget.data
    	finproj.deadline = form.deadline.data
    	if user == finproj.user_id:
    		db.session.add(finproj)
    		db.session.commit()
    		flash('You have successfully edited the project.')
    		
    		# redirect to the project page
    		return redirect(url_for('student.list_finprojs'))
    		
    	else:
    		flash('You can only edit the project you created.')
    		# redirect to the project page
    		return redirect(url_for('student.list_projtitles'))

   
    form.name.data = finproj.name
    form.category.data = finproj.category
    form.details.data = finproj.details
    form.budget.data = finproj.budget
    form.deadline.data = finproj.deadline
   
    return render_template('student/finprojs/finproj.html', action="Edit",
                           add_finproj=add_finproj, form=form,
                           finproj=finproj, title="Edit Project or Assignment")
                           
                           
# Internship Views

@student.route('student/internships', methods=['GET', 'POST'])
@login_required
def list_internships():
    """
    List all internships
    """
    check_student()

    internships = Internship.query.all()

    return render_template('student/intern/internships.html',
                           internships=internships, title="Internship Placements")
                           
# Interns views                          
@student.route('/student/interns', methods=['GET', 'POST'])
@login_required
def list_interns():
    """
    List all interns
    """
    check_student()

    interns = Intern.query.all()

    return render_template('student/intern/interns.html',
                           interns=interns, title="Interns")
                           
@student.route('/student/interns/add/<int:id>', methods=['GET', 'POST'])
@login_required
def apply_internship(id):
    """
    Add internship application to the database
    """
    check_student()
    interns = Intern.query.all()
    add_intern = True
    internship = Internship.query.get_or_404(id)
    form = InternForm()
    if form.validate_on_submit():  	
    	user = current_user.id
    	for inter in interns:
    		if inter.user_id == user and inter.internship_id == internship.id:
    			flash('You have already appiled for this internship placement.')
    			return redirect(url_for('student.list_internships'))
    			
    	interne = Intern(internship_id = internship.id, user_id = user, date = datetime.datetime.utcnow())
    	
    	try:
    		# add internship application to the database
    		db.session.add(interne)
    		db.session.commit()
    		flash('You have successfully applied for internship.')
    		return redirect(url_for('student.list_interns'))
    		
    	except:
    		# in case the application fails
    		flash('Error: the internship application was unsuccessful.')
    		
    		# redirect to the interns page
    		
    	

    # load interns template
    return render_template('student/intern/intern.html', action="Add",
                           apply_internship=apply_internship, form=form,
                           title="Apply for Internship")
    	
                           
# Research views                          
@student.route('/student/researchs', methods=['GET', 'POST'])
@login_required
def list_researchs():
    """
    List all research
    """
    check_student()

    researchs = Research.query.all()

    return render_template('student/researchs/researchs.html',
                           researchs=researchs, title="Available Research")

                      
# Projects views                          
@student.route('/student/getProjects', methods=['GET'])
@login_required
def getProjects():
    """
    Get all projects
    """
    check_student()

    projects = Project.query.all()
    projects_dict = []
    for project in projects:
    	project_dict = {'Id':project.id,
    					'Title':project.name,
    					'Description':project.description,
    					'Category':project.category.name,
    					'By':project.user.first_name,
    					
    					'FilePath':project.img_url}
    	projects_dict.append(project_dict)
    	
    return json.dumps(project_dict)
    
   

@student.route('/student/projects/list_projects', methods=['POST','GET'])
@login_required
def list_projects():
	"""
	list all projects
	"""
	return render_template('/student/projects/projects.html')
	
@student.route('/addUpdateLike', methods=[ 'POST', 'GET'])	
@login_required
def addUpdateLike(id):
    """
    Add, update like
    """
    check_inventor()
    
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    votes = Vote.query.all()
    user = current_user.id
    
    for vot in votes:
    	if vot.user_id == user:
    		flash('You have already voted for the project.')
    		return redirect(url_for(student.list_projects))
    vote = Vote(use_id = user, project_id = project.id)
    
    project.vote = project.vote + 1
    
    db.session.add(project)
    db.session.add(vote)
    db.session.commit()
    
    return json.dumps({'status':'OK'})

# Items views                          
@student.route('/student/items', methods=['GET', 'POST'])
@login_required
def list_items():
    """
    List all items
    """
    check_student()

    stock = Stock.query.all()

    return render_template('student/items/items.html',
                           stocks=stocks, title="Items")
                           
                           
# Project titles views                          
@student.route('/student/projecttitles', methods=['GET', 'POST'])
@login_required
def list_projtitles():
    """
    List all project titles
    """
    check_student()

    projtitles = Projtitle.query.all()

    return render_template('student/projects/projtitles.html',
                           projtitles=projtitles, title="Project Titles")

# Post a comment on project   
@student.route('/student/project/add/<int:id>', methods=['GET', 'POST'])
@login_required
def comment_project(id):
    """
    Post comment on a project
    """
    check_student()

    comments = Comment.query.all()
    project = Project.query.get_or_404(id)
    form = CommentForm()
    user = current_user.id
    if form.validate_on_submit():
    	comment = Comment(message = form.comment.data,
    						user_id = user,
    						date = datetime.datetime.utcnow(),
    						project_id = project.id)
    	try:
    		#Add comment to database
    		db.session.add(comment)
    		db.session.commit()
    		flash('Your comment has been posted')
    		
    	except:
    		#In case there is a problem
    		flash('Error: Your comment was not posted')
    		
    	#redirect to Projects page
    	return redirect(url_for('student.list_projects'))
    	
    #load post comment on project template
    return render_template('student/projects/projdisc.html', action="Add",
    						comment_project=comment_project, form=form, comments=comments,
    						title="Comment on Research Project")
    						
# Post a comment on research   
@student.route('/student/research/add/<int:id>', methods=['GET', 'POST'])
@login_required
def comment_research(id):
    """
    Post comment on a research
    """
    check_student()

    comments = Comment.query.all()
    research = Research.query.get_or_404(id)
    form = CommentForm()
    user = current_user.id
    if form.validate_on_submit():
    	comment = Comment(message = form.comment.data,
    						user_id = user,
    						date = datetime.datetime.utcnow(),
    						research_id = research.id)
    	try:
    		#Add comment to database
    		db.session.add(comment)
    		db.session.commit()
    		flash('Your comment has been posted')
    		
    	except:
    		#In case there is a problem
    		flash('Error: Your comment was not posted')
    		
    	#redirect to Projects page
    	return redirect(url_for('student.list_researchs'))
    	
    #load post comment on project template
    return render_template('student/researchs/research.html', action="Add",
    						comment_research=comment_research, form=form, research=research,
    						comments=comments,
    						title="Comment on Research Paper")
    	

