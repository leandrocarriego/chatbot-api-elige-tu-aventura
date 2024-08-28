from flask import request, Response, json, Blueprint, jsonify
from flasgger import swag_from

from src.services import start_adventure
from src.models import Node, Option
from src.config import Config, db, migrations, swagger_template, swagger_config

routes = Blueprint("actions", __name__)

@routes.route('/start', methods = ["POST"])
def start():
    """Inicia la aventura y devuelve la primera elección."""
    adventure_start = start_adventure()
    return jsonify(adventure_start), 200
