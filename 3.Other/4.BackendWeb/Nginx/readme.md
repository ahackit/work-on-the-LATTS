# Nginx

- NGINX is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more.
- nginx has one master process and several worker processes
  - The main purpose of the master process is to read and evaluate configuration, and maintain worker processes. 
  - Worker processes do actual processing of requests.
  - number of worker processes is defined in the configuration file and may be fixed for a given configuration or automatically adjusted to the number of available CPU cores

## Configuration
-  configuration file is named nginx.conf and placed in the directory /usr/local/nginx/conf, /etc/nginx, or /usr/local/etc/nginx.
- nginx consists of modules which are controlled by directives specified in the configuration file. 
  - Directives are divided into simple directives and block directives. 
  - A simple directive consists of the name and parameters separated by spaces and ends with a semicolon (;). 
  - A block directive has the same structure as a simple directive, but instead of the semicolon it ends with a set of additional instructions surrounded by braces ({ and }). 
  - If a block directive can have other directives inside braces, it is called a context
  - Directives placed in the configuration file outside of any contexts are considered to be in the main context.
- If changes made to running nginx need to ```-s reload```

## Controlling Nginx
```nginx -s signal```
- Signal = stop, quit, reload, reopen


## Serving Static Content
```
server {
    location / {
        root /data/www;
    }

    location /images/ {
        root /data;
    }
}
```

## Nginx as a Proxy Server
- which means a server that receives requests, passes them to the proxied servers, retrieves responses from them, and sends them to the clients.
```
server {
    location / {
        proxy_pass http://localhost:8080/;
    }

    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```