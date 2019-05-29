from flask import Flask  


def create_app(config_object):
    from .main import create_module_main

    app = Flask(__name__)
    app.config.from_object(config_object)
    
    create_module_main(app)

    return app