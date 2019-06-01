from flask import Blueprint, flash, render_template

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    static_folder='../static',
    url_prefix='/auth'
)

@auth_blueprint.route('login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_blueprint.route('register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')