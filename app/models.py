from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create an User table
    """
    
    #Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    sex = db.Column(db.String(10), index=True, nullable=False)	
    number1 = db.Column(db.String, index=True)
    number2 = db.Column(db.String, index=True)
    country = db.Column(db.String(60)) 
    password_hash = db.Column(db.String(128), nullable=False)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_inventor = db.Column(db.Boolean, default=False)
    is_student = db.Column(db.Boolean, default=False)
    projects = db.relationship('Project', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    researchs = db.relationship('Research', backref='user', lazy='dynamic')
    projtitles = db.relationship('Projtitle', backref='user', lazy='dynamic')
    finprojs = db.relationship('Finproj', backref='user', lazy='dynamic')
    interns = db.relationship('Intern', backref='user', lazy='dynamic')
    orders = db.relationship('Order', backref='user', lazy='dynamic')
    votes = db.relationship('Vote', backref='user', lazy='dynamic')
    doprojs = db.relationship('Doproj', backref='user', lazy='dynamic')
 
    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')
        
    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return '<User: {}>'.format(self.username)
        
#Set up user_loader
@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Project(db.Model):
    """
    Create a Project table
    """
    
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    description = db.Column(db.String(700))
    components = db.Column(db.String(700))
    instructions = db.Column(db.String(700))
    architecture = db.Column(db.String(700))
    assembly = db.Column(db.String(700))
    concept = db.Column(db.String(700))
    img_name = db.Column(db.String)
    img_url = db.Column(db.String, default=None)
    imgs = db.relationship('Img', backref='project', lazy='dynamic')
    videos = db.relationship('Video', backref='project', lazy='dynamic')
    documents = db.relationship('Document', backref='project', lazy='dynamic')
    vote = db.Column(db.Integer, default=0)	
    comments = db.relationship('Comment', backref='project', lazy='dynamic')
    votes = db.relationship('Vote', backref='project', lazy='dynamic')
    
    def __repr__(self):
        return '<Project: {}>'.format(self.name)

class Img(db.Model):
	"""
	Create Image table
	"""
	
	__tablename__ = 'imgs'
	id = db.Column(db.Integer, primary_key=True)
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
	research_id = db.Column(db.Integer, db.ForeignKey('researchs.id'), nullable=True)
	stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'), nullable=True)
	img_name = db.Column(db.String)
	img_url = db.Column(db.String, default=None)
    
class Video(db.Model):
	"""
	Create Video table
	"""
	
	__tablename__ = 'videos'
	id = db.Column(db.Integer, primary_key=True)
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
	research_id = db.Column(db.Integer, db.ForeignKey('researchs.id'), nullable=True)
	vid_name = db.Column(db.String)
	vid_url = db.Column(db.String, default=None)
    
class Document(db.Model):
	"""
	Create Document table
	"""
	
	__tablename__ = 'documents'
	id = db.Column(db.Integer, primary_key=True)
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
	research_id = db.Column(db.Integer, db.ForeignKey('researchs.id'), nullable=True)
	doc_name = db.Column(db.String)
	doc_url = db.Column(db.String, default=None)
       
class Category(db.Model):
    """
    Create a Category table
    """
    
    __tablename__ = 'categorys'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    details = db.Column(db.String(700))
    projects = db.relationship('Project', backref='category', lazy='dynamic')
    researchs = db.relationship('Research', backref='category', lazy='dynamic')
    projtitles = db.relationship('Projtitle', backref='category', lazy='dynamic')
    finprojs = db.relationship('Finproj', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return '<Category: {}>'.format(self.name)
        
class Comment(db.Model):
    """
    Create a Comments table
    """
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
    research_id = db.Column(db.Integer, db.ForeignKey('researchs.id'), nullable=True)
    projtitle_id = db.Column(db.Integer, db.ForeignKey('projtitles.id'), nullable=True)
    message = db.Column(db.String(700), nullable=False)
    date = db.Column(db.DateTime, nullable=False, )
    
    def __repr__(self):
        return '<Projdisc: {}>'.format(self.message)   

class Vote(db.Model):
    """
    Create a Vote table
    """
    
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    research_id = db.Column(db.Integer, db.ForeignKey('researchs.id'))
    
        
   
class Research(db.Model):
    """
    Create a Research table
    """
    
    __tablename__ = 'researchs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    details = db.Column(db.String(700))
    imgs = db.relationship('Img', backref='research', lazy='dynamic')
    videos = db.relationship('Video', backref='research', lazy='dynamic')
    documents = db.relationship('Document', backref='research', lazy='dynamic')
    vote = db.Column(db.Integer, default=0)
    date = db.column(db.DateTime)
    votes = db.relationship('Vote', backref='research', lazy='dynamic')
    comments = db.relationship('Comment', backref='research', lazy='dynamic')
    
    def __repr__(self):
        return '<Research: {}>'.format(self.name)
        
class Projtitle(db.Model):
    """
    Create a Projtitle table
    """
    
    __tablename__ = 'projtitles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    details = db.Column(db.String(700))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    date = db.Column(db.DateTime, nullable=False)
    comments = db.relationship('Comment', backref='projtitle', lazy='dynamic')
    
    def __repr__(self):
        return '<Projtitle: {}>'.format(self.name)
                

class Finproj(db.Model):
    """
    Create a Finproj table
    """
    
    __tablename__ = 'finprojs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    date = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    budget = db.Column(db.Integer)
    details = db.Column(db.String(700))
    doprojs = db.relationship('Doproj', backref='Finproj', lazy='dynamic')
    
    
    def __repr__(self):
        return '<Finproj: {}>'.format(self.name)
        
class Doproj(db.Model):
    """
    Create a Doproj table
    """
    
    __tablename__ = 'doprojs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    finproj_id = db.Column(db.Integer, db.ForeignKey('finprojs.id'))
    budget = db.Column(db.Integer)
    duration = db.Column(db.String(30))
    plan = db.Column(db.String(700))
    details = db.Column(db.String(700))
    
    
    def __repr__(self):
        return '<Doproj: {}>'.format(self.details)
        
class Internship(db.Model):
    """
    Create a Internship table
    """
    
    __tablename__ = 'internships'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    details = db.Column(db.String(700))
    objectives = db.Column(db.String(700))
    requirements = db.Column(db.String(700))
    outcomes = db.Column(db.String(700))
    duration = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    interns = db.relationship('Intern', backref='internship', lazy='dynamic')
    
    def __repr__(self):
        return '<Internship: {}>'.format(self.name)
        
class Intern(db.Model):
    """
    Create a Intern table
    """
    
    __tablename__ = 'interns'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'))
    date = db.Column(db.DateTime, nullable=False)   
    
    
    
    def __repr__(self):
        return '<Intern: {}>'.format(self.details)

class Stock(db.Model):
    """
    Create a stock table
    """
    
    __tablename__ = 'stocks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    details = db.Column(db.String(700))
    purpose = db.Column(db.String(700))
    unit_price = db.Column(db.Integer, nullable=False)
    img = db.relationship('Img', backref='stock', lazy='dynamic')
    orders = db.relationship('Order', backref='stock', lazy='dynamic')
    
    def __repr__(self):
        return '<Stock: {}>'.format(self.name)
        
class Order(db.Model):
    """
    Create a Log table
    """
    
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    date = db.Column(db.DateTime, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    
    
    
    def __repr__(self):
        return '<Log: {}>'.format(self.country)
    
    
   
        

	
        
        
