# APIs

- HTTP Endpoints should accept and response with JSON
- Endpoints should correspond to a resource or model in the database.
  - Resources can be nested articles/1/comments
- Use nons for endpoints, HTTP actions are your verbs.
  - GET retrieves resources. POST submits new data to the server. PUT updates existing data. DELETE removes data. The verbs map to the CRUD operations.
- Collections should be plural nouns
- Return standard error codes
- Should be able to filter/sort/and utilize pagination through query params
- Version your API.
- Cache Data

## Authentication
- Cookie based: Cookie-based authentication is stateful. This means that an authentication record or session must be kept both server and client-side. The server needs to keep track of active sessions in a database, while on the front-end a cookie is created that holds a session identifier, thus the name cookie based authentication.
- OAuth is an open-standard authorization protocol or framework that describes how unrelated servers and services can safely allow authenticated access to their assets without actually sharing the initial, related, single logon credential. In authentication parlance, this is known as secure, third-party, user-agent, delegated authorization. 
- Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the Authorization header that contains the word Basic word followed by a space and a base64-encoded string username:password .
- Token authentication requires users to obtain a computer-generated code (or token) before they're granted network entry. Token authentication is typically used in conjunction with password authentication for an added layer of security. This is what we refer to as two-factor authentication (2FA).
- Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token.

## Open API 
- OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection
- Use swagger