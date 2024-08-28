from flask import request, Response, json, Blueprint, jsonify
from pydantic import ValidationError

from src.services import choose_option
from src.api.v1.schemas import OptionRequest, NodeResponse

routes = Blueprint("options", __name__)

@routes.route('/choose', methods = ["POST"])
def choose():
    try:
        data = OptionRequest(**request.json)
        option_id = data.option_id
        response_data = choose_option(option_id)

        if response_data is None:
            return jsonify({"error": "Invalid option"}), 404
        
        response = NodeResponse(**response_data)
    
        return jsonify(response.dict()), 200

    except ValidationError as e:
        return jsonify(e.errors()), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 500
