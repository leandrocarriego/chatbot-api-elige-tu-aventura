from flask import Flask, Response, json
from flasgger import Swagger, LazyJSONEncoder

from .config import Config, db, migrations, swagger_template, swagger_config
from .api import api as api_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrations.init_app(app, db)
    
    from .models import Node, Option

    app.json_encoder = LazyJSONEncoder
    swagger = Swagger(app, template=swagger_template,config=swagger_config)

    @app.route('/', methods=["GET"])
    def home():
        return Response(
            response=json.dumps({'status': "success"}),
            status=200,
            mimetype='application/json'
        )

    app.register_blueprint(api_routes, url_prefix="/api")    
    
    return app

def run_server():
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)