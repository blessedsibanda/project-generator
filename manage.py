import os 
from webapp import create_app, db, migrate 
from webapp.api.hello.models import Greeting  

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, migrate=migrate, Greeting=Greeting)