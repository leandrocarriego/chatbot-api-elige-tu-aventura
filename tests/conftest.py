from flask import Flask
import pytest
from src.app import create_app
from src.config import Config, db, migrations
from src.api import api as api_routes
from common import seed_database


@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })

    db.init_app(app)
    migrations.init_app(app, db)
    
    from src.models import Node, Option

    app.register_blueprint(api_routes, url_prefix="/api")

    with app.app_context():
        db.create_all()
        seed_database(db)

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

