# Django

## Create Initial Project directory
 - django-admin startproject mysite - Creates basic files for Django
 - manage.py: CLI utility 
 - settings: Configuration for Django
 - urls: Routes for your website
 - asgi.py: Entry point for asgi-compatibable web servers
 - wsgi: Entry point for wsgi-compatitable web servers for your project

- ```python manage.py runserver``` -- to start dev server


## Helpful Manage.py commands
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py makemigrations
- python manage.py migrate
- python manage.py dbshell
- python manage.py shell
- python manage.py test APP

## Apps 
- Django organizes features and logic by Apps.
``` python manage.py startapp polls```

- Creates files for you
  - admin.py: where django admin logic goes
  - migrations: where db migrations goes
  - models: where db schema goes
  - tests: tests for individual app goes here
  - views: where all your endpoints go for your routes.

## Requests & Responses
- A typical view
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
- Create a urls file in your app directory
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
- In your main URLs files
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## Routes in Detail
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
## Templates
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

## Database Setup
- In settings.py you need to configure the DATABASE key

- To run initial database setup and future schema changes ``` python manage.py migrate```



## Models
- A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
- To Use your models they need to be seen in settings
```
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```
- Can then ```manage.py makemigrations``` and then ```manage.py migrate```

## Configuring Admin
- Need to register the model in Admin file to be used.
```
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

## Testing
```
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```