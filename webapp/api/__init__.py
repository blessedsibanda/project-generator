from flask_restful import Api 

from .hello.controllers import GreetingResource

rest_api = Api()

def create_module_api(app, **kwargs):
    rest_api.add_resource(
        GreetingResource,
        '/api/greeting',
        '/api/greeting/<int:greeting_id>'
    )
    rest_api.init_app(app)