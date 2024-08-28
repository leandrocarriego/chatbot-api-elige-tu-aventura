from flask import Flask, Response, json
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .api import api as api_routes


def run_server():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)

    @app.route('/', methods = ["GET"])
    def home():
        return Response(
            response=json.dumps({'status': "success"}),
            status=200,
            mimetype='application/json'
        )

    app.register_blueprint(api_routes, url_prefix = "/api" )

    app.run()