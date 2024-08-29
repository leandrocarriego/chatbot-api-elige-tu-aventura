from flask import request, Blueprint, jsonify
from pydantic import ValidationError

from src.services import choose_option
from src.api.v1.schemas import OptionRequest, NodeResponse


routes = Blueprint("options", __name__)

@routes.route('/choose', methods = ["POST"])
def choose():
    """
    Choose an option in the adventure.

    ---
    parameters:
        - name: option_id
          in: body
          required: true
          schema:
            type: object
            properties:
                option_id:
                    type: integer
                    description: The ID of selected option
    responses:
        200:
            description: Option chosen successfully
        404:
            description: Invalid option
        422:
            description: Validation error
        500:
            description: Server error
    """
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
