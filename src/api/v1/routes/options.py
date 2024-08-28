from flask import request, Response, json, Blueprint


routes = Blueprint("options", __name__)

@routes.route('/choose', methods = ["GET", "POST"])
def choose():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )
