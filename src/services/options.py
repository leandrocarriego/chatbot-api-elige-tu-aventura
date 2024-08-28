from src.models import Option


def choose_option(choice_id):
    """Función para manejar la elección del usuario."""
    option = Option.query.filter_by(id=choice_id).first()
    
    if not option:
        return None
    
    next_node = option.next_node
    return {
        "description": next_node.description,
        "options": [{"id": opt.id, "description": opt.description} for opt in next_node.options]
    }