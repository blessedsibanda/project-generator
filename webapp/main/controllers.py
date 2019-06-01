from flask import Blueprint, render_template
from flask_login import login_required

main_blueprint = Blueprint('main', 
                        __name__, 
                        template_folder='../templates/main',
                        static_folder='../static'
                    )

@main_blueprint.route('/')
def index():
    return render_template("index.html")

@main_blueprint.route('/protected')
@login_required
def confidential():
    return render_template("protected.html")