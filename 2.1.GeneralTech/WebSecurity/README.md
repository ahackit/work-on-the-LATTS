# LATT-WebSecurity
Learn All The Things - Web Secuirty

## HTTPS

Encrypted HTTP through use of certificates on the front and backend.

## CSP - Content Security Policy

Added layer of security that specifies where responses can come from.

https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP

## CORS - Cross Origin Resource Sharing

Notification when a web app from a differen origin (domain, protocol, port) is making a request to a server from a different origin.

Browsers restrict cross-origin http request by default from scripts.

https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

## OWASP Security Risks - Open Web Application Security Project

Internation non-profit org decided to web app security. They have a top 10 of biggest threats currently list.

### Injection

Injection attacks are code that is expected to be run by an interperter usually through form input. Like SQL escaped input.

Mitigate by sanitizing user-submitted data.

### Broken Authentication 

Typically when your authentication can be brute forced or has other issues. 

Mitigated by 2FA

### Sensitive Data Exposure

Man-in-the-middle attacks will get sensitive data. 

Mitigate by encrypt data and disable caching of sensitive info. 

### XML External Entities (XEE)

Attack against a web app that parses XML Input.

Mitigate by not using XML. Can also patch XML parsers and disable use of external entities.

### Broken Access Control

When your ACL is broken and/or exposed cuz of bad development.

Mitigate by using Auth Tokens.

### Security Misconfiguration. 

Using default configurations or displaying very verbose errors. 

Mitigate by not using defaults and making error messages more general.

### Cross-Site Scripting

When a web app allows users to add custom code into a URL path or on the website. 

Mitigation is escaping untrusted HTTP requests as well as validating/santizing user-generated content. 

### Inseucure Deserialization

When you packing and unpacking malicious data.

Mitigate with type checkings and monitoring, but really just don't deserialize data from untrusted source.

### Using Components with Known Vulnerabilities.

Tons of NPM packages out there. Could be bad code.

Mitigate by updating your stuff.

### Insufficient Logging And Monitoring

No logging and monitoring as well as incident response plans. 

Mitigate by adding logging and monitoring.

## MD5 and why not to use it

MD5 a cryptographic algo, often used to store passwords in DB. Produces a 32 character hexadecimal string any password.

### Why its no longer secure?

Brute force attacks are fast now

Dictionary tables are big now, most of the hashes are stored and can easily be searched. 

### How to Mitigate?

Use Md5 Salt

Use Long Passwords

Just other other sha functions / scrpyt or byscrpt


