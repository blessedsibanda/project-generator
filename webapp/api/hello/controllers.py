from flask import abort
from flask_restful import Resource, fields,marshal_with 
from webapp import db
from .models import Greeting
from .parsers import greeting_post_parser


greeting_fields = {
    'id': fields.Integer(),
    'greeting': fields.String(),
    'greeted_by': fields.String(),
    'created_on': fields.DateTime(dt_format='iso8601')
}

class GreetingResource(Resource):
    @marshal_with(greeting_fields)
    def get(self, greeting_id=None):
        if greeting_id:
            greeting = Greeting.query.get(greeting_id)
            if greeting:
                return greeting  
            abort(404)
        greetings = Greeting.query.all()
        return greetings

    @marshal_with(greeting_fields)
    def post(self):
        args = greeting_post_parser.parse_args(strict=True)
        new_greeting = Greeting(greeting=args['greeting'],
            greeted_by=args['greeted_by'])
        db.session.add(new_greeting)
        db.session.commit() 
        return new_greeting, 201