from flask import Flask
import pytest
from src.config import Config, db, migrations
from src.api import api as api_routes
from common import seed_database


@pytest.fixture(scope="session")
def test_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
        }
    )

    db.init_app(app)
    migrations.init_app(app, db)

    app.register_blueprint(api_routes, url_prefix="/api")

    with app.app_context():
        db.create_all()
        seed_database(db)

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture(scope="session")
def client(test_app): # pylint: disable=redefined-outer-name
    return test_app.test_client()
