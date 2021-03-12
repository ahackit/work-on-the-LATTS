# Caching

- Caching is the ability to store copies of frequently accessed data in several places along the request-response path. When a consumer requests a resource representation, the request goes through a cache or a series of caches (local cache, proxy cache, or reverse proxy) toward the service hosting the resource. 
- If any of the caches along the request path has a fresh copy of the requested representation, it uses that copy to satisfy the request. If none of the caches can satisfy the request, the request travels to the service (or origin server as it is formally known).

- GET requests should be cachable by default – until special condition arises. Usually, browsers treat all GET requests cacheable

- There are two main HTTP response headers that we can use to control caching behavior:
  -  Expires:  HTTP header specifies an absolute expiry time for a cached representation.
  - Cache-Control : core directive, introduced in the HTTP/1.1 standard, specifies whether a response’s contents can be cached, and if so, for how long. 
  - ETag : hash value that is specific to a given version of a resource. It can be used by the client in conjunction with the If-Match, If-None-Match, and If-Range headers to decide whether it should generate a new request for the latest version of a resource

## Server Side Caching
- Object caching – Storing database queries in a server-side cache for quick retrieval on subsequent page loads.
- CDN caching – A Content Delivery Network (CDN) is a cluster of servers that are geographically located all around the world. They cache content that’s loaded using the server that’s closest to the end user for much faster loading times.
- Opcode caching – PHP code is compiled between each request, then stored in a cache so it’s executable faster on repeated page loads.
- Redis rocks

### Django Caching
- Your cache preference goes in the CACHES setting in your settings file. 
- Supports many different options
  - Memcached is fastest? But temporary, server crash will lose it. Need to have mitigation strategy
- Once the cache is set up, the simplest way to use caching is to cache your entire site. You’ll need to add 'django.middleware.cache.UpdateCacheMiddleware' and 'django.middleware.cache.FetchFromCacheMiddleware' to your MIDDLEWARE setting, as in this example:
-  Set these three
  - CACHE_MIDDLEWARE_ALIAS – The cache alias to use for storage.
  - CACHE_MIDDLEWARE_SECONDS – The number of seconds each page should be cached.
  - CACHE_MIDDLEWARE_KEY_PREFIX – If the cache is shared across multiple sites using the same Django installation, set this to the name of the site, or some other string that is unique to this Django instance, to prevent key collisions. Use an empty string if you don’t care.

- Can cache Single Views
```
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    ...
```
```
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
```

## Client-Side Caching

- Use LocalStorage/cookies. Vue got libraries to help with it.