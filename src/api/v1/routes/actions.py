from flask import Blueprint, jsonify
from pydantic import ValidationError

from src.services import start_adventure
from src.api.v1.schemas import NodeResponse

routes = Blueprint("actions", __name__)

@routes.route('/start', methods = ["POST"])
def start():
    try:
        response_data = start_adventure()

        if response_data is None:
            return jsonify({"error": "Data no exists"}), 404
        
        response = NodeResponse(**response_data)
    
        return jsonify(response.dict()), 200

    except ValidationError as e:
        return jsonify(e.errors()), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 500
