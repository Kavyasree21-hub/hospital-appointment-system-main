from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from application.database import db
import os

api = Api()

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.secret_key = "secret123"

    if os.getenv("ENV", "development") == "production":
        raise Exception("Production not configured")
    else:
        app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    api.init_app(app)

    with app.app_context():
        from application import controller
        from application import api as api_routes

    return app
