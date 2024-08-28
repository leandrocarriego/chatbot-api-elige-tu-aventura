from flask import Blueprint

from .v1.routes import routes as v1_routes


api = Blueprint( 'api' , __name__)

api.register_blueprint(v1_routes, url_prefix= "/v1" )
