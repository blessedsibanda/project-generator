from flask_restful import reqparse

# post requests    <resource>_<http-method>_parser
greeting_post_parser = reqparse.RequestParser() 
greeting_post_parser.add_argument(
    'greeting',
    type=str,
    required=True,
    help='greeting is required',
    location=('json', 'values')
)
greeting_post_parser.add_argument(
    'greeted_by',
    type=str,
    required=True,
    help='greeted_by is required',
    location=('json', 'values')
)