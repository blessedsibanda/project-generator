from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message = 'Please login to access this page'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    from .models import User 
    return User.query.get(user_id)

def authenticate(username, password):
    from .models import User 
    user = User.query.filter_by(username=username).first()
    if not user:
        return None 
    # do the passwords match
    if not user.check_password(password):
        return None 
    return user

def create_module_auth(app, **kwargs):

    bcrypt.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)

