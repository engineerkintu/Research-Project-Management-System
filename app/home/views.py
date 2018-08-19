from flask import abort, render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")
    
@home.route('/inventor/dashboard')
@login_required
def inventor_dashboard():
    if not current_user.is_inventor:
        abort(403)
    return render_template('home/inventor_dashboard.html', title="Dashboard")

@home.route('/student/dashboard')
@login_required
def student_dashboard():
    if not current_user.is_student:
        abort(403)
    return render_template('home/student_dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html', title="Dashboard")
