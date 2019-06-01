from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def create_module_auth(app, **kwargs):
    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)