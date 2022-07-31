from flask import Blueprint
myblueprint = Blueprint('myblueprint',__name__,template_folder='template')
from . import routes
