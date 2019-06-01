from flask_restful import Api 

from .hello.controllers import GreetingResource


def create_module_api(app, **kwargs):
    rest_api = Api(app)
    rest_api.add_resource(
        GreetingResource, 
        '/api/greeting/<int:greeting_id>',
        '/api/greeting'
    )