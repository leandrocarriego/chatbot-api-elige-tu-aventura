from flask import request, Response, json, Blueprint


routes = Blueprint("actions", __name__)

@routes.route('/start', methods = ["GET"])
def start():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )
