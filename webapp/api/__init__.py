from flask_restful import Api 

from .hello.controllers import GreetingResource, GreetingsResource


def create_module_api(app, **kwargs):
    rest_api = Api(app)
    rest_api.add_resource(
        GreetingResource, '/api/greeting/<int:greeting_id>'
    )
    rest_api.add_resource(
        GreetingsResource,'/api/greeting'
    )
