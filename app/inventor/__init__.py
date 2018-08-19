from flask import Blueprint

inventor = Blueprint('inventor', __name__)

from . import views
