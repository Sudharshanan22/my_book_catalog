from flask import Blueprint
auth_blueprint = Blueprint('auth_blueprint',__name__,template_folder='template')
from . import routes
