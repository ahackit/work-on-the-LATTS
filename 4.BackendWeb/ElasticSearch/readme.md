# Elasticsearch

- ES is a NoSQL DB
- Stores data in a unstructured way
- Elasticsearch has a strong focus on search capabilities and features — so much so, in fact, that the easiest way to get data from ES is to search for it using the extensive Elasticsearch API.
-  you can configure general settings (e.g. node name), as well as network settings (e.g. host and port), where data is stored, memory, log files, and more in config file
- ES is a service that needs started
- Should be able to hit 9200

## Indexing
- Indexing is process of adding data to ES
- Operates like a rest api so PUT or POST data to is.
- Check indexes
``` curl -XGET 'localhost:9200/_cat/indices?v&pretty' ```

## Querying
- Can get data through GET
``` curl -XGET 'localhost:9200/app/users/4?pretty' ```
- _Meta is internal ES stuff
- Can query searches by hitting
``` curl -XGET 'localhost:9200/_search?q=logged' ```
- Can use query params to filter
  - username:johnb – Looks for documents where the username field is equal to “johnb”
  - john* – Looks for documents that contain terms that start with john and is followed by zero or more characters such as “john"
  - john? - Looks for documents that contain terms that start with john followed by only one character.

## DSL
- Can also retrieve data using request bodies
  - 1) leaf query clauses that look for a value in a specific field
  - 2) compound query clauses (which might contain one or several leaf query clauses). 

## Delete Data
```  curl -XDELETE 'localhost:9200/logs?pretty' ```