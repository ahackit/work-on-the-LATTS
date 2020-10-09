# Django

## Models
- A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
- To Use your models they need to be seen in settings
```
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```