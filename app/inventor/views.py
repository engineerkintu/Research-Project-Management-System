# app/inventor/views.py


from flask import abort, flash, redirect, render_template, url_for, request, make_response, Response, redirect
from flask_login import current_user, login_required

from . import inventor
from ..inventor.forms import ProjectForm, CategoryForm, ResearchForm, ProjtitleForm, CommentForm
from .. import db
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, Comment
from app import videos, documents, images

import datetime

def check_inventor():
    """
    Prevent non-inventors from accessing the page
    """
    if not current_user.is_inventor:
        abort(403)

# Project Views

@inventor.route('inventor/projects', methods=['GET', 'POST'])
@login_required
def list_projects():
    """
    List all projects
    """
    check_inventor()

    projects = Project.query.all()

    return render_template('inventor/projects/projects.html',
                           projects=projects, title="Projects")
def view_project():
    """
    View the project details
    """
    check_inventor()
    
    return render_template('inventor/projects/projectview.html',
                           projects=projects, title="Project View")

@inventor.route('inventor/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
    """
    Add a project to the database
    """
    check_inventor()

    add_project = True

    form = ProjectForm()
    if form.validate_on_submit():
    	
    	user = current_user.id
    	project = Project(name=form.name.data,
    	                  category = form.category.data,
    	                  user_id = user,
    	                  instructions = form.instructions.data,
    	                  architecture = form.architecture.data,
    	                  components = form.components.data,
    	                  assembly = form.assembly.data,
    	                  concept = form.concept.data,
    	                  description=form.description.data)
    	
    	try:
    		# add project to the database
    		db.session.add(project)
    		db.session.commit()
    		flash('You have successfully added a new project.')
    	except:
    		# in case department name already exists
    		flash('Error: project name already exists.')
    		
    	# redirect to departments page
    	return redirect(url_for('inventor.list_projects'))

    # load department template
    return render_template('inventor/projects/project.html', action="Add",
                           add_project=add_project, form=form,
                           title="Add Project")
    	

@inventor.route('inventor/projects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """
    Edit a project
    """
    check_inventor()

    add_project = False

    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    user = current_user.id
    if form.validate_on_submit():
       
        if user == project.user_id:
            project.name = form.name.data
            project.description = form.description.data
            project.category_id = form.category.data
            project.instructions = form.instructions.data
            project.architecture = form.architecture.data
            project.components = form.components.data
            project.concept = form.concept.data
           
            db.session.add(project)
            db.session.commit()
            flash('You have successfully edited the project.')
            
            # redirect to the projects page
            return redirect(url_for('inventor.list_projects'))
            
        else:
            flash('You can only edit the project you created.')
            # redirect to the projects page
            return redirect(url_for('inventor.list_projects'))

    form.description.data = project.description
    form.name.data = project.name
    form.category.data = project.category_id
    form.instructions.data = project.instructions
    form.architecture.data = project.architecture
    form.components.data = project.components
    form.concept.data = project.concept
   
    return render_template('inventor/projects/project.html', action="Edit",
                           add_project=add_project, form=form,
                           project=project, title="Edit Project")
                           
# Category Views

@inventor.route('inventor/categorys', methods=['GET', 'POST'])
@login_required
def list_categorys():
    """
    List all categorys
    """
    check_inventor()

    categorys = Category.query.all()

    return render_template('inventor/categorys/categorys.html',
                           categorys=categorys, title="Categorys")

@inventor.route('inventor/categorys/add', methods=['GET', 'POST'])
@login_required
def add_category():
    """
    Add a category to the database
    """
    check_inventor()

    add_category = True

    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data,       
                          details=form.details.data)
        try:
            # add category to the database
            db.session.add(category)
            db.session.commit()
            flash('You have successfully added a new category.')
        except:
            # in case category name already exists
            flash('Error: category name already exists.')

        # redirect to categorys page
        return redirect(url_for('inventor.list_categorys'))

    # load category template
    return render_template('inventor/categorys/category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Category")
                           
# Research Views

@inventor.route('inventor/researchs', methods=['GET', 'POST'])
@login_required
def list_researchs():
    """
    List all researchs
    """
    check_inventor()

    researchs = Research.query.all()

    return render_template('inventor/researchs/researchs.html',
                           researchs=researchs, title="Research")
def view_research():
    """
    View the research details
    """
    check_inventor()
    
    return render_template('inventor/researchs/researchview.html',
                           researchs=researchs, title="Research View")

@inventor.route('inventor/researchs/add', methods=['GET', 'POST'])
@login_required
def add_research():
    """
    Add a research to the database
    """
    check_inventor() 

    add_research = True

    form = ResearchForm()
    if form.validate_on_submit():
    	fil = documents.save(request.files['doc_file'])
    	fil_url = documents.url(fil)   	
    	user = current_user.id
    	research = Research(name=form.name.data,
    						category = form.category.data,
    						user_id = user,
    						details = form.details.data,
    						file_name = fil,
    						file_url = fil_url,
    						date = datetime.datetime.utcnow())
    	
    	try:
    		# add research to the database
    		db.session.add(research)
    		db.session.commit()
    		flash('You have successfully added a new research.')
    	except:
    		# in case research name already exists
    		flash('Error: project title name already exists.')
    		
    	# redirect to researchs page
    	return redirect(url_for('inventor.list_researchs'))

    # load research template
    return render_template('inventor/researchs/research.html', action="Add",
                           add_research=add_research, form=form,
                           title="Add Research")
    	

@inventor.route('inventor/researchs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_research(id):
    """
    Edit a research
    """
    check_inventor()

    add_research = False

    research = Research.query.get_or_404(id)
    form = ResearchForm(obj=research)
    user = current_user.id
    if form.validate_on_submit():
    	research.name = form.name.data
    	research.details = form.details.data
    	research.category = form.category.data
    	if user == research.user_id:
    		db.session.add(research)
    		db.session.commit()
    		flash('You have successfully edited your research.')
    		
    		# redirect to the researchs page
    		return redirect(url_for('inventor.list_researchs'))
    		
    	else:
    		flash('You can only edit a research you created.')
    		# redirect to the researchs page
    		return redirect(url_for('inventor.list_researchs'))

   
    form.name.data = research.name
    form.category.data = research.category
    form.details.data = research.details
    
   
    return render_template('inventor/researchs/research.html', action="Edit",
                           add_research=add_research, form=form,
                           research=research, title="Edit Research")
                           
# Project Title Views

@inventor.route('inventor/projtitles', methods=['GET', 'POST'])
@login_required
def list_projtitles():
    """
    List all project titles
    """
    check_inventor()

    projtitles = Projtitle.query.all()

    return render_template('inventor/titles/titles.html',
                           projtitles=projtitles, title="Project title")
def view_projtitle():
    """
    View the project title details
    """
    check_inventor()
    
    return render_template('inventor/titles/titleview.html',
                           projtitles=projtitles, title="Project title View")

@inventor.route('projtitles/add', methods=['GET', 'POST'])
@login_required
def add_projtitle():
    """
    Add a project title to the database
    """
    check_inventor() 

    add_projtitle = True
    user = current_user.id
    form = ProjtitleForm()
    if form.validate_on_submit():
    	projtitle = Projtitle(name=form.name.data,
    						  details = form.details.data,
    						  user_id = user,
    						  date = datetime.datetime.utcnow(),
    						  category = form.category.data)
    	
    	try:
    		# add project title to the database
    		db.session.add(projtitle)
    		db.session.commit()
    		flash('You have successfully added a new project title.')
    	except:
    		# in case project title is not added
    		flash('Error: project title was not added to database.')
    		
    	# redirect to project titles page
    	return redirect(url_for('inventor.list_projtitles'))

    # load project title template
    return render_template('inventor/titles/title.html', action="Add",
                           add_projtitle=add_projtitle, form=form,
                           title="Add Project Title")
    	

@inventor.route('inventor/projtitles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_projtitle(id):
    """
    Edit a project title
    """
    check_inventor()

    add_projtitle = False

    projtitle = Projtitle.query.get_or_404(id)
    form = ProjtitleForm(obj=projtitle)
    user = current_user.id
    if form.validate_on_submit():
    	projtitle.name = form.name.data
    	projtitle.details = form.details.data
    	projtitle.category = form.category.data
    	if user == projtitle.user_id:
    		db.session.add(projtitle)
    		db.session.commit()
    		flash('You have successfully edited the project title.')
    		
    		# redirect to the projtitles page
    		return redirect(url_for('inventor.list_projtitles'))
    		
    	else:
    		flash('You can only edit the project title you created.')
    		# redirect to the projtitles page
    		return redirect(url_for('inventor.list_projtitles'))

   
    form.name.data = projtitle.name
    form.category.data = projtitle.category
    form.details.data = projtitle.details
    
   
    return render_template('inventor/titles/title.html', action="Edit",
                           add_projtitle=add_projtitle, form=form,
                           projtitle=projtitle, title="Edit Project Title")


