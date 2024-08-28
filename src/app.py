from flask import Flask, Response, json

from .api import api as api_routes


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

app.register_blueprint(api_routes, url_prefix = "/api" )