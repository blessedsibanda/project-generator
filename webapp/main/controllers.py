from flask import Blueprint, render_template

main_blueprint = Blueprint('main', 
                        __name__, 
                        template_folder='../templates/main',
                        static_folder='../static'
                    )

@main_blueprint.route('/')
def index():
    return render_template("index.html")