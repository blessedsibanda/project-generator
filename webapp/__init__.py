from flask import Flask  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

from config import app_config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_name):
    from .main import create_module_main
    from .api import create_module_api
    from .auth import create_module_auth

    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    create_module_main(app)
    create_module_auth(app)
    create_module_api(app)

    return app