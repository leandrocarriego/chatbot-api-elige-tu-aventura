from flask import Blueprint, Response

from .actions import routes as actions_routes
from .options import routes as options_routes


routes = Blueprint('v1_routes', __name__)


@routes.route('/', methods=["GET"])
def api_home():
    """
    This is the home endpoint of the API.

    ---
    responses:
        200:
            description: Successful
        500:
            description: Server error
    """
    return Response(status=200)

routes.register_blueprint(actions_routes)
routes.register_blueprint(options_routes)
