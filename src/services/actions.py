from src.models import Node


def start_adventure():
    first_node = Node.query.filter_by(id=1).first()
    if not first_node:
        return {"error": "No starting node found"}
    
    return {
        "description": first_node.description,
        "options": [{"id": option.id, "description": option.description} for option in first_node.options]
    }