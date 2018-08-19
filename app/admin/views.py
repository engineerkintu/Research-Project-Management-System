# app/admin/views.py


from flask import abort, flash, redirect, render_template, url_for, request, make_response, Response, redirect
from flask_login import current_user, login_required

from . import admin

from ..admin.forms import InternshipForm, StockForm, UserForm
from .. import db
from ..models import Project, Category, Research, Projtitle, Finproj, Doproj, Internship, Stock, User, Intern
from app import images, videos, documents

import datetime

def check_admin():
    """
    Prevent non-administrators from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Internship Views

@admin.route('admin/internships', methods=['GET', 'POST'])
@login_required
def list_internships():
    """
    List all internships
    """
    check_admin()

    internships = Internship.query.all()

    return render_template('admin/internships/internships.html',
                           internships=internships, title="Internship Placements")


@admin.route('admin/internships/add', methods=['GET', 'POST'])
@login_required
def add_internship():
    """
    Add an internship placement to the database
    """
    check_admin() 

    add_internship = True

    form = InternshipForm()
    if form.validate_on_submit():
    	internship = Internship(name=form.name.data,
    	                  details = form.details.data,
    	                  objectives = form.objectives.data,
    	                  requirements = form.requirements.data,
    	                  outcomes = form.outcomes.data,
    	                  duration = form.duration.data,
    	                  start_date = datetime.datetime.utcnow()
    	                  )
    	
    	try:
    		# add an internship placement to the database
    		db.session.add(internship)
    		db.session.commit()
    		flash('You have successfully added a new internship placement.')
    	except:
    		# in case internship is not added
    		flash('Error: internship placement was not added to database.')
    		
    	# redirect to items page
    	return redirect(url_for('admin.list_internships'))

    # load stock template
    return render_template('admin/internships/internship.html', action="Add",
                           add_internship=add_internship, form=form,
                           title="Add Internship Placement")

@admin.route('admin/internships/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_internship(id):
    """
    Edit a internship
    """
    check_admin()

    add_internship = False

    internship = Internship.query.get_or_404(id)
    form = InternshipForm(obj=internship)
    if form.validate_on_submit():
        internship.name = form.name.data
        internship.details = form.details.data
        internship.objectives = form.objectives.data
        internship.requirements = form.requirements.data
        internship.outcomes = form.outcomes.data
        internship.duration = form.duration.data
        db.session.commit()
        flash('You have successfully edited the internship placement.')

        # redirect to the internships page
        return redirect(url_for('admin.list_internships'))

    form.details.data = internship.details
    form.name.data = internship.name
    form.objectives.data = internship.objectives
    form.requirements.data = internship.requirements
    form.outcomes.data = internship.outcomes
    form.duration.data = internship.duration
    return render_template('admin/internships/internship.html', action="Edit",
                           add_internship=add_internship, form=form,
                           internship=internship, title="Edit Internship")

@admin.route('admin/internships/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_internship(id):
    """
    Delete an internship from the database
    """
    check_admin()

    internship = Internship.query.get_or_404(id)
    db.session.delete(internship)
    db.session.commit()
    flash('You have successfully deleted an intership.')

    # redirect to the internships page
    return redirect(url_for('admin.list_internships'))

    return render_template(title="Delete Internship")
    
# Stock Views

@admin.route('admin/stock', methods=['GET', 'POST'])
@login_required
def list_stocks():
    """
    List all items in stock
    """
    check_admin()

    stocks = Stock.query.all()

    return render_template('admin/stocks/stocks.html',
                           stocks=stocks, title="Items fo Sell")
def view_stock():
    """
    View the item details
    """
    check_admin()
    
    return render_template('admin/stocks/stockview.html',
                           researchs=researchs, title="Item View")

@admin.route('admin/stocks/add', methods=['GET', 'POST'])
@login_required
def add_stock():
    """
    Add a stock to the database
    """
    check_admin() 

    add_stock = True

    form = StockForm()
    if form.validate_on_submit():
    	fil = images.save(request.files['img'])
    	fil_url = images.url(fil)  	
    	
    	stock = Stock(name=form.name.data,
    	                  details = form.details.data,
    	                  purpose = form.purpose.data,
    	                  unit_price = form.unit_price.data,
    	                  image_filename = fil,
    	                  image_url = fil_url,
    	                  )
    	
    	try:
    		# add item to the database
    		db.session.add(stock)
    		db.session.commit()
    		flash('You have successfully added a new item.')
    	except:
    		# in case item is not added
    		flash('Error: item was not added to database.')
    		
    	# redirect to items page
    	return redirect(url_for('admin.list_stocks'))

    # load stock template
    return render_template('admin/stocks/stock.html', action="Add",
                           add_stock=add_stock, form=form,
                           title="Add Item")
    	
@admin.route('admin/stocks/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_stock(id):
    """
    Edit a stock
    """
    check_admin()

    add_stock = False

    stock = Stock.query.get_or_404(id)
    form = StockForm(obj=stock)
    if form.validate_on_submit():
        stock.name = form.name.data
        stock.details = form.details.data
        stock.purpose = form.purpose.data
        stock.unit_price = form.unit_price.data
        db.session.add(stock)
        db.session.commit()
        flash('You have successfully edited the stock.')

        # redirect to the stocks page
        return redirect(url_for('admin.list_stocks'))

    form.details.data = stock.details
    form.name.data = stock.name
    form.purpose.data = stock.purpose
    form.unit_price.data = stock.unit_price
    return render_template('admin/stocks/stock.html', add_stock=add_stock,
                           form=form, title="Edit Item in Stock")
                           
@admin.route('admin/stocks/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_stock(id):
    """
    Delete a stock from the database
    """
    check_admin()

    stock = Stock.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the item from stock.')

    # redirect to the stocks page
    return redirect(url_for('admin.list_stocks'))

    return render_template(title="Delete Stock")
    
# Users Views

@admin.route('admin/user', methods=['GET', 'POST'])
@login_required
def list_users():
    """
    List all users in stock
    """
    check_admin()

    stocks = Stock.query.all()

    return render_template('admin/stocks/stocks.html',
                           stocks=stocks, title="Items fo Sell")
def view_user():
    """
    View the item details
    """
    check_admin()
    
    return render_template('admin/stocks/stockview.html',
                           researchs=researchs, title="Item View")
                           
@admin.route('admin/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def block_user(id):
    """
    Edit a stock
    """
    check_admin()

    

    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
    	if form.block.data == 'Block':
    		if user.is_student == True:
    			user.is_student = False
    		elif user.is_inventor == True:
    			user.is_inventor = False
    		else:
    			flash('User already bloacked')
    	else:
    		if user.is_student == False:
    			user.is_student = True
    		elif user.is_inventor == False:
    			user.is_inventor = True
    	db.session.add(user)
    	db.session.commit()
    	flash('You have successfully edited the user.')
    	
    	# redirect to the users page
    	return redirect(url_for('admin.list_users'))

    
    return render_template('admin/users/user.html', block_user=block_user,
                           form=form, title="Block User")

# Research projects Views

@admin.route('admin/projects', methods=['GET', 'POST'])
@login_required
def list_projects():
    """
    List all research projects
    """
    check_admin()

    projects = Project.query.all()

    return render_template('admin/projects/projects.html',
                           projects=projects, title="Research Projects")
                           
@admin.route('admin/projects/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    """
    Delete a research project from the database
    """
    check_admin()

    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('You have successfully deleted a research project.')

    # redirect to the projects page
    return redirect(url_for('admin.list_projects'))

    return render_template(title="Delete Research Project")
    
# Research papers Views

@admin.route('admin/researchs', methods=['GET', 'POST'])
@login_required
def list_researchs():
    """
    List all research papers
    """
    check_admin()

    researchs = Research.query.all()

    return render_template('admin/researchs/researchs.html',
                           researchs=researchs, title="Research Papers")
                           
@admin.route('researchs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_research(id):
    """
    Delete a research paper from the database
    """
    check_admin()

    research = Research.query.get_or_404(id)
    db.session.delete(research)
    db.session.commit()
    flash('You have successfully deleted a research project.')

    # redirect to the research papers page
    return redirect(url_for('admin.list_researchs'))

    return render_template(title="Delete Research Paper")
    

# Categories Views

@admin.route('categorys', methods=['GET', 'POST'])
@login_required
def list_categorys():
    """
    List all categories
    """
    check_admin()

    categorys = Category.query.all()

    return render_template('admin/categorys/categorys.html',
                           researchs=researchs, title="Categories")
                           
@admin.route('categorys/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    """
    Delete a category from the database
    """
    check_admin()

    category = Category.query.get_or_404(id)
    db.session.delete(research)
    db.session.commit()
    flash('You have successfully deleted a category.')

    # redirect to the categories page
    return redirect(url_for('admin.list_categorys'))

    return render_template(title="Delete Categories")

# Student Project Views

@admin.route('finprojs', methods=['GET', 'POST'])
@login_required
def list_finprojs():
    """
    List all student projects
    """
    check_admin()

    finprojs = Finproj.query.all()

    return render_template('admin/finprojs/finprojs.html',
                           finprojs=finprojs, title="Student Projects")
                           
@admin.route('finprojs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_finproj(id):
    """
    Delete a student project from the database
    """
    check_admin()

    finproj = Finproj.query.get_or_404(id)
    db.session.delete(finproj)
    db.session.commit()
    flash('You have successfully deleted a student project.')

    # redirect to the student projects page
    return redirect(url_for('admin.list_finprojs'))

    return render_template(title="Delete Student Project")

# Project title Views

@admin.route('projtitles', methods=['GET', 'POST'])
@login_required
def list_projtitles():
    """
    List all student projects
    """
    check_admin()

    projtitles = Projtitle.query.all()

    return render_template('admin/projtitles/projtitles.html',
                           projtitles=projtitles, title="Project Titles")
                           
@admin.route('projtitles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_projtitle(id):
    """
    Delete a project title from the database
    """
    check_admin()

    projtitle = Projtitle.query.get_or_404(id)
    db.session.delete(projtitle)
    db.session.commit()
    flash('You have successfully deleted a project title.')

    # redirect to the project titles page
    return redirect(url_for('admin.list_projtitles'))

    return render_template(title="Delete Project Title")
    
    
# Internship application Views

@admin.route('interns', methods=['GET', 'POST'])
@login_required
def list_interns():
    """
    List all internship applications
    """
    check_admin()

    interns = Intern.query.all()

    return render_template('admin/interns/interns.html',
                           interns=interns, title="Internship Applications")
                           
@admin.route('interns/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_intern(id):
    """
    Delete an intern from the database
    """
    check_admin()

    interne = Intern.query.get_or_404(id)
    db.session.delete(interne)
    db.session.commit()
    flash('You have successfully deleted an interne.')

    # redirect to the project titles page
    return redirect(url_for('admin.list_interns'))

    return render_template(title="Delete Intern")
