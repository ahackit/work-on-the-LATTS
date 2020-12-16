from chalice import Chalice
# from marshmallow import Schema, fields
from peewee import *
from marshmallow_peewee import ModelSchema
pg_db = PostgresqlDatabase('postgres', user='postgres', password='sifting123!',
                           host='rds.amazonaws.com', port=5432)
class Person(Model):
    name = CharField()

    class Meta:
        database = pg_db # This model uses the "people.db" database.

class PersonSchema(ModelSchema):

    class Meta:
        model = Person

app = Chalice(app_name='marshmellowtest')
app.debug = True

def initialize_db():
    pg_db.connect()
    pg_db.create_tables([Person], safe = True)
    pg_db.close()


@app.route('/')
def index():
    initialize_db()
    Person.create(name='Austin')
    query = Person.select().where(Person.name == 'Austin').get()
    schema = PersonSchema()
    return schema.dump(query)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
