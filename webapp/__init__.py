from flask import Flask  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    from .main import create_module_main
    from .api import create_module_api

    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    
    create_module_main(app)
    create_module_api(app)

    return app