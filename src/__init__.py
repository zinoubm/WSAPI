# environment
import os
from flask import Flask
from src.constants.http_status_codes import HTTP_404_NOT_FOUND

# data base
from src.database import db, History

# blueprints
from src.auth import auth
from src.compare import compare


def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # development configuration
        app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
            JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
        )
    
    else:
        # testing configuration
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    # blueprint registration
    app.register_blueprint(auth)
    app.register_blueprint(compare)

    # home pagecompare
    @app.get('/')
    def home():
        return {'msg':'welcome to our API'}

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def headle_not_found(e):
        return {'error':'page not found'}

    return app