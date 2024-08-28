from flask import request, Response, json, Blueprint, jsonify

from src.services import choose_option


routes = Blueprint("options", __name__)

@routes.route('/choose', methods = ["POST"])
def choose():
    """Recibe la elección del usuario y devuelve las siguientes opciones o el resultado final."""
    data = request.json
    choice_id = data.get('choice_id')
    
    if choice_id is None:
        return jsonify({"error": "choice_id is required"}), 400
    
    result = choose_option(choice_id)
    
    if result is None:
        return jsonify({"error": "Invalid choice"}), 404
    
    return jsonify(result), 200
