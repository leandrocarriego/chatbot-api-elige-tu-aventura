from flask import Blueprint 

from .actions import routes as actions_routes
from .options import routes as options_routes


routes = Blueprint('v1_routes' , __name__) 

routes.register_blueprint(actions_routes)
routes.register_blueprint(options_routes)
