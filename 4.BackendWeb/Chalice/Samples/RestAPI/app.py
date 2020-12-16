from chalice import Chalice, NotFoundError, BadRequestError, Response
# * BadRequestError - return a status code of 400
# * UnauthorizedError - return a status code of 401
# * ForbiddenError - return a status code of 403
# * NotFoundError - return a status code of 404
# * ConflictError - return a status code of 409
# * UnprocessableEntityError - return a status code of 422
# * TooManyRequestsError - return a status code of 429
# * ChaliceViewError - return a status code of 500

app = Chalice(app_name='restapitest')
# app.debug = True


CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR'
}

@app.route('/')
def index():
    return {'hello': 'world'}

# URL Routing
@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (city, ', '.join(CITIES_TO_STATE.keys())))

# Put Methods
@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {"value": value}

# Multiple HTTP Verbs
@app.route('/resource/{value}', methods=['POST','PUT'])
def myview():
    pass

#Separate Functions for the same route with different verbs
@app.route('/resource/{value}', methods=['POST','PUT'])
def myview_put():
    pass

@app.route('/resource/{value}', methods=['POST','PUT'])
def myview_post():
    pass

#Request Metadata
# current_request.query_params - A dict of the query params.
# current_request.headers - A dict of the request headers.
# current_request.uri_params - A dict of the captured URI params.
# current_request.method - The HTTP method (as a string).
# current_request.json_body - The parsed JSON body.
# current_request.raw_body - The raw HTTP body as bytes.
# current_request.context - A dict of additional context information
# current_request.stage_vars - Configuration for the API Gateway stage
#to_dict
OBJECTS = {
}

@app.route('/objects/{key}', methods=['GET', 'PUT'])
def myobject(key):
    request = app.current_request
    if request.method == 'PUT':
        OBJECTS[key] = request.json_body
    elif request.method == 'GET':
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)

# Request Content Types

import sys

from urllib.parse import urlparse, parse_qs



@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def index():
    parsed = parse_qs(app.current_request.raw_body.decode())
    return {    
        'states': parsed.get('states', [])
    }

# HTTP Response Objects
@app.route('/')
def index():
    return Response(body='hello world!', status_code=200, headers={'Content-Type': 'text/plain'})

# CORS Support
# For Globa: app.api.cors = True.

@app.route('/supports-cors', methods=['PUT'], cors=True)
def supports_cors():
    return {}

# cors_config = CORSConfig(
#     allow_origin='https://foo.example.com',
#     allow_headers=['X-Special-Header'],
#     max_age=600,
#     expose_headers=['X-Special-Header'],
#     allow_credentials=True
# )
# @app.route('/custom-cors', methods=['GET'], cors=cors_config)
# def supports_custom_cors():
#     return {'cors': True}