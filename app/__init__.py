from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import DevelopmentConfig, TestingConfig, ProductionConfig

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name="development"):
    app = Flask(__name__)

    if config_name == "production":
        app.config.from_object(ProductionConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)

    from app.routes import members_bp
    app.register_blueprint(members_bp)

    return app
