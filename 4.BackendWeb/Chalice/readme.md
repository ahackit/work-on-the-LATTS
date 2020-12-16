# Chalice 

## AWS Credentials
-  Need to have /.aws/config with ENV variables

## Install

 - `pip install chalice`

## Creating new project
- `chalice new-project project_name`

## Chalice Folder Strucutre
- .chalice folder
  - Configuration
- app.py
  - Where main code goes
- chalicelib
  - Extra code for other files
- requirements.txt
  - Packages for Chalice to Install

## Deploying
- `chalice deploy`

## Clean up
- `chalice delete`

## Using Chalice
### Routes
- Follows flask paradigms
- use `Chalice.route('/)` to construct routes and Lambda functions
  - No trailing /'s
- Can capture url parameters via
```
@app.route('/users/{name}')
def users(name):
    return {'name': name}

from chalice import Chalice

app = Chalice(app_name='helloworld')


@app.route('/a/{first}/b/{second}')
def users(first, second):
    return {'first': first, 'second': second}
```

- use `app.current_request` to see other request metadata. 
```
@app.route('/users/{name}')
def users(name):
    result = {'name': name}
    if app.current_request.query_params.get('include-greeting') == 'true':
        result['greeting'] = 'Hello, %s' % name
    return result
```

### View Functions
- A function that is attached to the @app.route() decorator
- View functiosn take no parameters unless specified in the route.
- Can return several types of return options
  - `Response`
  - `bytes` must have a `Content-Type` that's present in `app.api.binary_types`
  - Any other return type is sent back as JSON with content/type `application/json`
  - `ChaliceViewError` and all of it's subclasses

#### Error Handling
- BadRequestError- returns a status code of 400
- UnauthorizedError- returns a status code of 401
- ForbiddenError- returns a status code of 403
- NotFoundError- returns a status code of 404
- ConflictError- returns a status code of 409
- TooManyRequestsError- returns a status code of 429
- ChaliceViewError- returns a status code of 500

```
from chalice import Chalice
from chalice import BadRequestError

app = Chalice(app_name="badrequest")

@app.route('/badrequest')
def badrequest():
    raise BadRequestError("This is a bad request")
```

#### Specifying HTTP Methods
- `@app.route('/resource/{value}', methods=['PUT'])`
- Can have multiple methods in a single list
- or have different named views corresponding to the same route with different methods for varying logic
  - Must have different view function names
  - Must not override the same http method
  - Must have same CORS config

#### General Recommendations
- No need to use `Response` if just returning JSON as it's default
- Use `Response` when returnning non-json content or need to inject custom headers
- For errors, use the built in `ChaliceViewError` subclasses

### Configuration File
- Can configure chalice with the `.config` file
- We can configure Stages in the config file (dev, beta, prod), and have different configurations based on stage
- Can specify `api_gateway_endpoint_type` (edge,regional, private)
- `api_gateway_endpoint_vpce` when configuring a Private API a VPC Endpoint id must be specified to configure a default resource policy on the API if an explicit policy is not specified. 
- `api_gateway_policy_file`: file pointing to an IAM resource policy for the REST API.
  - If not provided, chalice auto-generates when private. 
  - File is relative to .chalice
- `api_gateway_stage`: The name of the API gateway stage. This will also be the URL prefix for your API
- `autogen_policy`: boolean value that indicates if chalice should try to automatically generate an IAM policy based on analyzing your application source code.
  - If False, chalice will try to load a local file `.chalice/policy-<stage-name>.json`
- `environment_variables`: mapping of key value pairs. These key value pairs will be set as environment variables in your application. All environment variables must be strings. 
  - If this key is specified in both a stage specific config option as well as a top level key, the stage specific environment variables will be merged into the top level keys.
- `iam_policy_file`: overrides the local IAM policy file when not auto-generating
- `iam_role_arn`: Only used if `manage_iam_role` is false, but specifys which ARN to use when configuring the app
- `lambda_memory_size`: integer repesenting amount of memory, in MB, your lambda function is gven. Must be multiple of 64MB, default is 128.
- `lambda_timeout`: How long a Lambda is allowed to run before timing out, default is 60 seconds
- `layers`: list of the Lambda Layers ARNs. Can provide at a per stage as well as per function level.
- `automatic_layer`: Chalice can attempt to construct a single stage layer for all lambda functions with requirements.txt and vendored libraries. Defaults to false
- `api_gateway_custom_domain`: Mapping of key value pairs. Has required values
  - `domain_name`: custom domain name to associate with REST API
  - `certificate_arn`: the ARN of ACM certificate for the current domain name.
    - If you are using `REGIONAL` endpoint, the ACM Cert must be in the same region as your API. If `EDGE`, must be US-East-1
  - OPTIONAL
  - `tls_version`: TLS version of the security policy for this domain name
  - `url_prefix`: allows you to add prefix after your domain name
- `websocket_api_custom_domain`: Same as `api_gateway_custom_domain`
- `manage_iam_role`: true/false, indicate if you want chalice to create and update the IAM role used for your app.
- `minimum_compression_size`: integer value that indicates the minimum compression size to apply to the API gateway. Stage specific keys override the others
- `reserved_concurrency`: integer representing each function’s reserved concurrency. This value can be provided per stage as well as per Lambda function
- `subnet_ids`: list of subnet ids for VPC configuration. This value can be provided per stage as well as per Lambda function. In order for this value to take effect, you must also provide the security_group_ids value. When both values are provided and autogen_policy is True, chalice will automatically update your IAM role with the necessary permissions to create, describe, and delete ENIs.
- `security_group_ids`: list of security groups for VPC configuration. This value can be provided per stage as well as per Lambda function.

#### Lambda Specifc Configuration
- Can also config things not just at Chalice Stage lage, but per lamda function
- Chalice app can have many stages, stage can have many lambda's
- Lambda config at stage Level
```
    {
        "version": "2.0",
        "app_name": "app",
        "stages": {
            "dev": {
            "lambda_functions": {
                "foo": {
                "lambda_timeout": 120
                }
            }
            }
        }
    }
```
- Can specify across all stages
    ```
    {
    "version": "2.0",
    "app_name": "app",
    "lambda_functions": {
        "foo": {
        "lambda_timeout": 120
        }
    }
    }
    ```
- Values that can be configured
  - autogen_policy
  - environment_variables
  - iam_policy_file
  - iam_role_arn
  - lambda_memory_size
  - lambda_timeout
  - layers
  - manage_iam_role
  - reserved_concurrency
  - security_group_ids
  - subnet_ids
  - tags

#### Custom Domain Name example
```
{
  "version": "2.0",
  "app_name": "app",
  "stages": {
    "dev": {
      "autogen_policy": true,
      "api_gateway_stage": "dev"
      "api_gateway_custom_domain": {
        "domain_name": "api.example.com",
        "security_policy": "TLS 1.2|TLS 1.0",
        "certificate_arn": "arn:aws:acm:example.com",
        "url_prefixes": ["foo", "bar],
        "tags": {
          "key": "tag1",
          "key1": "tag2"
        }
      },
    },
  }
}
```

#### IAM Roles and Policies per Stage
```
{
  "version": "2.0",
  "app_name": "app",
  "stages": {
    "dev": {
      "autogen_policy": true,
      "api_gateway_stage": "dev"
    },
    "beta": {
      "autogen_policy": false,
      "iam_policy_file": "beta-app-policy.json"
    },
    "prod": {
      "manage_iam_role": false,
      "iam_role_arn": "arn:aws:iam::...:role/prod-role"
    }
  }
}
```

#### ENV Variables configuration
```
{
  "version": "2.0",
  "app_name": "app",
  "environment_variables": {
    "SHARED_CONFIG": "foo",
    "OTHER_CONFIG": "from-top"
  },
  "stages": {
    "dev": {
      "environment_variables": {
        "TABLE_NAME": "dev-table",
        "OTHER_CONFIG": "dev-value"
      }
    },
    "prod": {
      "environment_variables": {
        "TABLE_NAME": "prod-table",
        "OTHER_CONFIG": "prod-value"
      }
    }
  }
}
```

#### Per Lambda Configuration
```
{
  "stages": {
    "dev": {
      "environment_variables": {
        "OWNER": "dev-team"
      }
      "api_gateway_stage": "api",
      "lambda_functions": {
        "foo": {
          "subnet_ids": ["sn-1", "sn-2"],
          "security_group_ids": ["sg-10", "sg-11"],
          "layers": ["layer-arn-1", "layer-arn-2"],
        },
        "bar": {
          "manage_iam_role": false,
          "iam_role_arn": "arn:aws:iam::my-role-name",
          "environment_variables": {"TABLE_NAME": "mytable"}
        }
      }
    }
  },
  "version": "2.0",
  "app_name": "demo"
}
```

### Multifile Support
- All your code doesn't have to sit in app.py
- can structure that code under `chalicelib` directory
  - Can have other files besides .py files. Can have binary assets, and .jsons, etc
```
//chalicelib/__init__.py
MESSAGE = 'world'

//app.py
from chalice import Chalice
from chalicelib import MESSAGE

app = Chalice(app_name="multifile")

@app.route("/")
def index():
    return {"hello": MESSAGE}
```

### Logging
- can use any of the options available to lambda functions as outlined in the AWS Lambda Docs. 
-  The simplest option is to just use print statements. 
-  Anything you print will be accessible in cloudwatch logs as well as in the output of the chalice logs command.
- Chalice offers a special logger
- can access this logger via the app.log attribute
  - StreamHandler associated with sys.stdout.
  - Log level set to logging.ERROR by default. You can also manually set the logging level by setting app.log.setLevel(logging.DEBUG).
  - A logging formatter that displays the app name, level name, and message.
```
from chalice import Chalice

app = Chalice(app_name='demolog')


@app.route('/')
def index():
    app.log.debug("This is a debug statement")
    app.log.error("This is an error statement")
    return {'hello': 'world'}
```
```
from chalice import Chalice

app = Chalice(app_name='multilog')


@app.lambda_function()
def foo(event, context):
    app.log.debug("Invoking from function foo")
    return {'hello': 'world'}


@app.lambda_function(name='MyFunction)
def bar(event, context):
    incr_counter()
    app.log.debug("Invoking from function bar")
    return {'hello': 'world'}

$ chalice logs --name foo
$ chalice logs --name MyFunction
```

### SDK Generation
- Chalice offers a `chalice generate-sdk` command that will automatically generate an SDK based on your declared routes.
- Basically a quick way of exporting out some JavaScript for you to use. 

### Stages
- Chalice Stages != AWS Resources.
- Chalice instantly creates a dev stage by default. 
- You can build out multiple stages and deploy using `chalice deploy --stage prod`

### Packaging Your App
- zip file is created that contains your application and all third party packages your application requires. 
- This file is used by AWS Lambda and is referred to as a deployment package.
- Chalice also has the ability to split your code into multiple files to leverage AWS Lambda layers.

#### 3rd Party Packages
- Can have packages in `requirements.txt`
- Can also place in `vendor`, these are great for packages that can't be pip installed

#### Automatic Lambda Layers
- set `automatic layer` to true
  - The layer is created once and then shared across all Lambda functions in your application.
  - When creating or updating a Lambda function, you send the entire contents of the zip file that contains your app. This is repeated for each Lambda function. As a result, there is unnecessary time and network bandwidth used to send the same 3rd party dependencies for each Lambda function. When using layers, Chalice will specify the layer ARN when creating or updating your Lambda function, which cuts down on the time it takes to package and deploy your application.
  - Saves storage space in Lambda. There is a 75GB maximum size for all your Lambda functions. If you’re not using layers, each Lambda function stores its own copies of your 3rd party dependencies.

### AWS CloudFormation Support
- Chalice uses `boto3` when you use `chalice deploy`
- Can also use `chalice package` so you can manage deployments yourself using AWSCLI and CloudFormation
- chalice will generate the AWS Lambda deployment package that contains your application as well as a Serverless Application Model (SAM) template
- you can’t switch between chalice deploy and chalice package + CloudFormation for deploying your app.

#### Template Merging
- common use case to need to modify a Chalice generated template before deployment. Often to inject extra resources, values, or configurations that are not supported directly by Chalice. 
- `$ chalice package --merge-template extras.json out`
```
{
  "Resources" : {
    "MusicTable" : {
      "Type" : "AWS::DynamoDB::Table",
      "Properties" : {
        "TableName" : "MusicData",
        "AttributeDefinitions" : [
          {
            "AttributeName" : "Album",
            "AttributeType" : "S"
          },
          {
            "AttributeName" : "Artist",
            "AttributeType" : "S"
          }
        ],
        "KeySchema" : [
          {
            "AttributeName" : "Album",
            "KeyType" : "HASH"
          },
          {
            "AttributeName" : "Artist",
            "KeyType" : "RANGE"
          }
        ],
        "ProvisionedThroughput" : {
          "ReadCapacityUnits" : "5",
          "WriteCapacityUnits" : "5"
        }
      }
    },
    "APIHandler": {
      "Properties": {
        "Environment": {
          "Variables": {
            "MUSIC_TABLE": {"Ref": "MusicTable"}
          }
        }
      }
    }
  }
}
```
- CloudFormation commands
```
$ pip install chalice awscli
$ chalice new-project test-cfn-deploy
$ cd test-cfn-deploy
chalice package /tmp/packaged-app/
aws cloudformation package \
     --template-file /tmp/packaged-app/sam.json \
     --s3-bucket myapp-bucket \
     --output-template-file /tmp/packaged-app/packaged.yaml
aws cloudformation deploy \
    --template-file /tmp/packaged-app/packaged.yaml \
    --stack-name test-cfn-stack \
    --capabilities CAPABILITY_IAM
aws cloudformation describe-stacks --stack-name test-cfn-stack \
  --query "Stacks[].Outputs[?OutputKey=='EndpointURL'][] | [0].OutputValue"
```
### Authorization
- Has multiple ways to support Auth
- All authorizers are configured per-route using the `authorizer` kwarg to an `@app.route()`

#### AWS IAM Auth
```
from chalice import IAMAuthorizer

authorizer = IAMAuthorizer()

@app.route('/iam-auth', methods=['GET'], authorizer=authorizer)
def authenticated():
    return {"success": True}
```

#### Cognito User Pools
```
from chalice import CognitoUserPoolAuthorizer

authorizer = CognitoUserPoolAuthorizer(
    'MyPool', provider_arns=['arn:aws:cognito:...:userpool/name'])

@app.route('/user-pools', methods=['GET'], authorizer=authorizer)
def authenticated():
    return {"success": True}
```

#### Custom Auth
```
from chalice import CustomAuthorizer

authorizer = CustomAuthorizer(
    'MyCustomAuth', header='Authorization',
    authorizer_uri=('arn:aws:apigateway:region:lambda:path/2015-03-31'
                    '/functions/arn:aws:lambda:region:account-id:'
                    'function:FunctionName/invocations'))

@app.route('/custom-auth', methods=['GET'], authorizer=authorizer)
def authenticated():
    return {"success": True}
```

#### Built-in Authorizers
- Previous Auths are for when you have existing authorizers
- Built-in is a way to write custom authorizers in Chalice
- Need to use `@app.authorizer()` and take single arg of `AuthRequest`. Will return a `AuthResponse`
```
from chalice import Chalice, AuthResponse

app = Chalice(app_name='demoauth1')


@app.authorizer()
def demo_auth(auth_request):
    token = auth_request.token
    # This is just for demo purposes as shown in the API Gateway docs.
    # Normally you'd call an oauth provider, validate the
    # jwt token, etc.
    # In this exampe, the token is treated as the status for demo
    # purposes.
    if token == 'allow':
        return AuthResponse(routes=['/'], principal_id='user')
    else:
        # By specifying an empty list of routes,
        # we're saying this user is not authorized
        # for any URLs, which will result in an
        # Unauthorized response.
        return AuthResponse(routes=[], principal_id='user')


@app.route('/', authorizer=demo_auth)
def index():
    return {'context': app.current_request.context}
```

### Lambda Event Sources
#### Scheduled Events
- Periodacally invoke a lambda function based on regular schedule
```
app = chalice.Chalice(app_name='foo')

@app.schedule('rate(1 hour)')
def every_hour(event):
    print(event.to_dict())
```
- Chalice will create the necessary CloudWatch event/rules
- Must accept an `event` argument
- Can have multiple scheduled events

#### CloudWatch Events
- Subscribe to any cloudwatch event
```
app = chalice.Chalice(app_name='foo')

@app.on_cw_event({"source": ["aws.codecommit"]})
def on_code_commit_changes(event):
    print(event.to_dict())
```

#### S3 Events
- Configure a lambda function to invoke when certain events happen in S3 Bucket. Uses `Event notifications` provided by S3
```
from chalice import Chalice

app = chalice.Chalice(app_name='s3eventdemo')
app.debug = True

@app.on_s3_event(bucket='mybucket-name',
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
```

#### SNS Events
- Chalice will automatically handle creating the lambda function, subscribing the lambda function to the SNS topic, and modifying the lambda function policy to allow SNS to invoke the function.
```
pip install boto3
import boto3
sns = boto3.client('sns')
sns.create_topic(Name='my-demo-topic')
@app.on_sns_message(topic='my-demo-topic')
def handle_sns_message(event):
    app.log.debug("Received message with subject: %s, message: %s",
                  event.subject, event.message)
```
- Publish an event
```
import boto3
sns = boto3.client('sns')
topic_arn = [t['TopicArn'] for t in sns.list_topics()['Topics']
              if t['TopicArn'].endswith(':my-demo-topic')][0]
sns.publish(Message='TestMessage1', Subject='TestSubject1',
             TopicArn=topic_arn)
```

#### SQS Events
-  configure a lambda function to be invoked whenever messages are available on an SQS queue
-  Use `Chalice.on_sqs_message()`
-  message visibility timeout of your SQS queue must be greater than or equal to the lambda timeout. The default message visibility timeout when you create an SQS queue is 30 seconds, and the default timeout for a Lambda function is 60 seconds, so you’ll need to modify one of these values in order to successfully connect an SQS queue to a Lambda function.
```
aws sqs get-queue-attributes \
    --queue-url https://us-west-2.queue.amazonaws.com/1/testq \
    --attribute-names VisibilityTimeout

aws sqs set-queue-attributes \
    --queue-url https://us-west-2.queue.amazonaws.com/1/testq \
    --attributes VisibilityTimeout=60
```
```
from chalice import Chalice

app = chalice.Chalice(app_name='chalice-sqs-demo')
app.debug = True

@app.on_sqs_message(queue='my-queue', batch_size=1)
def handle_sqs_message(event):
    for record in event:
        app.log.debug("Received message with contents: %s", record.body)
```
- Use `my-queue.fifo` for first in and out

#### Kinesis Events
```
from chalice import Chalice

app = chalice.Chalice(app_name='kinesiseventdemo')
app.debug = True

@app.on_kinesis_record(stream='mystream')
def handle_kinesis_message(event):
    for record in event:
        # The .data attribute is automatically base64 decoded for you.
        app.log.debug("Received message with contents: %s", record.data)
```

#### DynamoDB Events
```
from chalice import Chalice

app = chalice.Chalice(app_name='ddb-event-demo')
app.debug = True

@app.on_dynamodb_record(stream_arn='arn:aws:dynamodb:.../stream/2020')
def handle_ddb_message(event):
    for record in event:
        app.log.debug("New: %s", record.new_image)
```

### Pure Lambda
- chalice also supports managing pure Lambda functions that don’t have any abstractions built on top.
- useful if you want to create a Lambda function for something that’s not supported by chalice or if you just want to create Lambda functions but don’t want to manage handling dependencies and deployments yourself.
- `Chalice.lambda_function()`
```
app = chalice.Chalice(app_name='foo')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.lambda_function()
def custom_lambda_function(event, context):
    # Anything you want here.
    return {}

@app.lambda_function(name='MyFunction')
def other_lambda_function(event, context):
    # Anything you want here.
    return {}
```

### Blueprints
- used to organize app into logical components. Similar to Blueprints in Flask
- Blueprints can have all resources like the main Chalice App
```
$ chalice new-project blueprint-demo
$ cd blueprint-demo
$ mkdir chalicelib
$ touch chalicelib/__init__.py
$ touch chalicelib/blueprints.py
```
```
// chalicelib/blueprints.py
from chalice import Blueprint

extra_routes = Blueprint(__name__)

@extra_routes.route('/foo')
def foo():
    return {'foo': 'bar'}
```
```
//app.py
from chalice import Chalice
from chalicelib.blueprints import extra_routes

app = Chalice(app_name='blueprint-demo')
app.register_blueprint(extra_routes)


@app.route('/')
def index():
    return {'hello': 'world'}
```
- `app.register_blueprint` can have `name_prefix` and `url_prefix`.
- If you specify url_prefix, any routes defined in your blueprint will have the url_prefix prepended to it. 
- If you specify the name_prefix, any Lambda functions created will have the name_prefix prepended to the resource name.

### Websockets
- Still considered experimental, so need to use experimental flag
```
app = Chalice('myapp')
app.experimental_feature_flags.update([
    'WEBSOCKETS'
])
```
- In a Chalice app the websocket API is accessed through the three decorators `on_ws_connect`, `on_ws_message`, `on_ws_disconnect`.
- decorated websocket handler function takes one argument `event` with the type WebsocketEvent.
```
from boto3.session import Session
from chalice import Chalice

app = Chalice(app_name='test-websockets')
app.experimental_feature_flags.update([
    'WEBSOCKETS',
])
app.websocket_api.session = Session()


@app.on_ws_connect()
def connect(event):
    print('New connection: %s' % event.connection_id)


@app.on_ws_message()
def message(event):
    print('%s: %s' % (event.connection_id, event.body))


@app.on_ws_disconnect()
def disconnect(event):
    print('%s disconnected' % event.connection_id)
```
#### Sending a Message
```
from boto3.session import Session
from chalice import Chalice

app = Chalice(app_name='test-websockets')
app.experimental_feature_flags.update([
    'WEBSOCKETS',
])
app.websocket_api.session = Session()


@app.on_ws_message()
def message(event):
    app.websocket_api.send(event.connection_id, 'I got your message!')
```

### Custom Domain Names
- Must have AWS cert or imported cert
- Custom domain names can be configured per Chalice stage
- First you must configure your Chalice app such that it creates the necessary resources and configuration when provisioning your REST or WebSocket APIs
- Then you must configure your DNS configuration to point your custom domain name to the domain name created by API Gateway. 
- API Gateway, Rest API
```
{
    "stages": {
        "dev": {
            "api_gateway_stage": "api",
            "api_gateway_custom_domain": {
                "domain_name": "api.example.com",
                "tls_version": "TLS_1_2|TLS_1_0",
                "certificate_arn": "arn:aws:acm:example",
                "url_prefix": "foo",
                "tags": {
                    "key": "tag1",
                    "key1": "tag2"
                }
            }
        }
    }
}
```
- API Gateway, WebSockets
```
{
    "stages": {
        "dev": {
            "api_gateway_stage": "api",
            "websocket_api_custom_domain": {
                "domain_name": "api.example.com",
                "tls_version": "TLS_1_2|TLS_1_0",
                "certificate_arn": "arn:aws:acm:example",
                "url_prefix": "foo",
                "tags": {
                    "key": "tag1",
                    "key1": "tag2"
                }
            }
        }
    }
}
```
- Need to manually configure your DNS through AWS CLI or Console

### Testing
- `chalice.test` is test client
#### Lambda Functions
```
/app.py
from chalice import Chalice

app = Chalice(app_name="testclient")

@app.lambda_function()
def foo(event, context):
    return {'hello': 'world'}

@app.lambda_function()
def bar(event, context):
    return {'event': event}
```
```
//tests/test_appy/
from chalice.test import Client
from app import app

def test_foo_function():
    with Client(app) as client:
        result = client.lambda_.invoke('foo')
        assert result.payload == {'hello': 'world'}

def test_bar_function():
    with Client(app) as client:
        result = client.lambda_.invoke(
            'bar', {'my': 'event'})
        assert result.payload == {'event': {'my': 'event'}}
```
```
pip install pytest
py.test tests/test_app.py
```
#### Specific Events
```
from chalice import Chalice

@app.on_sns_message(topic='mytopic')
def foo(event):
    return {'message': event.message}

# Test code

from chalice.test import Client

def test_sns_handler():
    with Client(app) as client:
        response = client.lambda_.invoke(
            "foo",
            client.events.generate_sns_event(message="hello world")
        )
        assert response.payload == {'message': 'hello world'}
```
#### ENV Variables
```
from chalice import Chalice

app = Chalice(app_name="testclient")

@app.lambda_function()
def foo(event, context):
    return {'value': os.environ.get('MY_ENV_VAR')}

@app.lambda_function()
def bar(event, context):
    return {'value': os.environ.get('MY_ENV_VAR')}

 # Test code
from chalice.test import Client

def test_foo_function():
    with Client(app, stage_name='prod') as client:
        result = client.lambda_.invoke('foo')
        assert result.payload == {'value': 'TOP LEVEL'}

def test_bar_function():
    with Client(app) as client:
        result = client.lambda_.invoke('bar')
        assert result.payload == {'value': 'OVERRIDE'}
```
#### Rest APIS
```
from chalice.test import Client
from app import app

 def test_index():
     with Client(app) as client:
         response = client.http.get('/')
         assert response.json_body == {'hello': 'world'}
```
##### With Authorizers
```
from chalice import Chalice

app = Chalice(app_name="testclient")

@app.authorizer()
def myauth(event)
    if event.token == 'allow':
        return AuthResponse(['*'], principal_id='id')
    return AuthResponse([], principal_id='noone')

@app.route('/needs-auth', authorizer=myauth)
def needs_auth()
    return {'success': True}

#  Test code:
from chalice.test import Client

 def test_needs_auth():
     with Client(app) as client:
         response = client.http.get(
             '/needs-auth', headers={'Authorization': 'allow'})
         assert response.json_body == {'success': True}
         assert client.http.get(
             '/needs-auth',
             headers={'Authorization': 'deny'}).status_code == 403
```
#### Boto3 Stubber
```
from chalice.test import Client
import app

from botocore.stub import Stubber

def test_calls_rekognition():
    client = app.get_rekognition_client()
    stub = Stubber(client)
    stub.add_response(
        'detect_labels',
        expected_params={
            'Image': {
                'S3Object': {
                    'Bucket': 'mybucket',
                    'Name': 'mykey',
                }
            },
            'MinConfidence': 50.0,
        },
        service_response={
            'Labels': [
                {'Name': 'Dog', 'Confidence': 75.0},
                {'Name': 'Mountain', 'Confidence': 80.0},
                {'Name': 'Snow', 'Confidence': 85.0},
            ]
        },
    )
    with stub:
        with Client(app.app) as client:
            event = client.events.generate_s3_event(
                bucket='mybucket', key='mykey')
            response = client.lambda_.invoke('handle_object_created', event)
            assert response.payload == ['Dog', 'Mountain', 'Snow']
        stub.assert_no_pending_responses()
```

#### Pytest Fixtures
```
import app
from pytest import fixture
from chalice.test import Client

@fixture
def test_client():
    with Client(app.app) as client:
        yield client
```
```
def test_foo_function(test_client):
    result = test_client.lambda_.invoke('foo')
    assert result.payload == {'hello': 'world'}

def test_bar_function(test_client):
    result = test_client.lambda_.invoke(
        'bar', {'my': 'event'})
    assert result.payload == {'event': {'my': 'event'}}
```
- Or fixture on Boto3 Stubber
```
import app
from pytest import fixture
from chalice.test import Client


@fixture
def test_client():
    with Client(app.app) as client:
        yield client


@fixture
def rekognition_stub():
    client = app.get_rekognition_client()
    stub = Stubber(client)
    with stub:
        yield stub


def test_calls_rekognition(test_client, rekognition_stub):
    rekognition_stub.add_response(
        'detect_labels',
        expected_params={
            'Image': {
                'S3Object': {
                    'Bucket': 'mybucket',
                    'Name': 'mykey',
                }
            },
            'MinConfidence': 50.0,
        },
        service_response={
            'Labels': [
                {'Name': 'Dog', 'Confidence': 75.0},
                {'Name': 'Mountain', 'Confidence': 80.0},
                {'Name': 'Snow', 'Confidence': 85.0},
            ]
        },
    )
    event = test_client.events.generate_s3_event(
        bucket='mybucket', key='mykey')
    response = test_client.lambda_.invoke('handle_object_created', event)
    assert response.payload == ['Dog', 'Mountain', 'Snow']
    stub.assert_no_pending_responses()
```

### MiddleWare
- Allows you to alter the requst and response lifecycle. 
```
from chalice import Chalice

app = Chalice(app_name='demo-middleware')

@app.middleware('all')
def my_middleware(event, get_response):
    app.log.info("Before calling my main Lambda function.")
    response = get_response(event)
    app.log.info("After calling my main Lambda function.")
    return response

@app.route('/')
def index():
    return {'hello': 'world'}

@app.on_sns_message('mytopic')
def sns_handler(event):
    pass
```
#### Writing Middleware
- Must be a callable object that accepts two parameters, an event, and a get_response function.
- Must return a response.
- In order to invoke the next middleware in the chain and eventually call the actual Lambda handler, it must invoke get_response(event)
- Middleware can short-circuit the request be returning its own response. It does not have to invoke get_response(event) if not needed.
```
@app.middleware('all')
def noop_middleware(event, get_response):
    # The `event` type will depend on what type of
    # Lambda handler is being invoked.
    return get_response(event)
```

#### Error Handling
- With the exception of middleware for REST APIs, all middleware follow the same error handling strategy.
- Any exceptions from a Lambda handler are propagated back to each middleware. 
```
@app.middleware('all')
def handle_errors(event, get_response):
    try:
        return get_response(event)
    except MyCustomError as e:
        # We don't want MyCustomError to propagate, instead
        # we'll convert this to an error response dictionary.
        return {"Error": e.__class__.__name__,
                "Message": str(e)}

@app.lambda_function()
def noop_middleware(event, context):
    raise MyCustomError("Raising an error.")
```

##### Rest APIS
- middleware for Rest APIs won’t see exceptions propagate, they will instead see a Response object as a result of calling get_response(event).
```
from chalice import ChaliceUnhandledError

@app.middleware('all')
def handle_errors(event, get_response):
    try:
        return get_response(event)
    except ChaliceUnhandledError as e:
        return Response(status_code=500, body=str(e),
                        headers={'Content-Type': 'text/plain'})

@app.route('/')
def index():
    # The handle_errors middleware will never see this exception.
    # This will automatically be converted to a ``Response`` object
    # with a status code of ``500``.
    raise MyCustomError("Raising an error.")

@app.route('/error')
def unhandled_error():
    # The handle_errors middleware will see this exception because it's
    # of type ChaliceUnhandledError.
    raise ChaliceUnhandledError("Raising an error.")
```

#### Registering MiddleWare
```
all - Any
s3 - S3Event
sns - SNSEvent
sqs - SQSEvent
cloudwatch - CloudWatchEvent
scheduled - CloudWatchEvent
websocket - WebsocketEvent
http - Request
pure_lambda - LambdaFunctionEvent
```

#### Examples
- Short Circuiting a Request
```
from chalice Response

@app.middleware('http')
def require_header(event, get_response):
    # From the list above, because this is an ``http`` event
    # type, we know that event will be of type ``chalice.Request``.
    if 'X-Custom-Header' not in event.headers:
        return Response(
            status_code=400,
            body={"Error": "Missing required 'X-Custom-Header'"})
    # If the header exists then we'll defer to our normal request flow.
    return get_response(event)
```
- Modifying a Response
```
import time

@app.middleware('pure_lambda')
def inject_time(event, get_response):
    start = time.time()
    response = get_response(event)
    total = time.time() - start
    response.setdefault('metadata', {})['duration'] = total
    return response
```
