from src.models import Option


def choose_option(option_id):
    option = Option.query.filter_by(id=option_id).first()

    if not option:
        return None

    next_node = option.next_node
    return {
        "description": next_node.description,
        "options": [{"id": opt.id, "description": opt.description} for opt in next_node.options]
    }
