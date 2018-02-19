"""
-We first import the url function from the django.conf.urls.
-Then we import the views module
"""
from django.conf.urls import url
from . import views
"""
We then create a list named urlpatterns. This will a list of all
url instances of our app.

We create the Url instance by calling the url function. We pass in
the Url regular expression, the view and the name keyword.

Note
1.Regex
- ^ denotes the start of a string.
- $ denotes the end of a string

2. View.
Once Django finds a match it calls the specified view function.
It passes in the HttpRequest object as the first argument.

I.e if the regex captures a value it passes it to the app view
function as positional arguments

3. Name
Naming the url allows us to refer to it from elsewhere in our app.

Below we add additional urls to navigate to news according to date
it was posted.

got this error when didn't put parenthesis around \d{4}-\d{2}-\d{2}

----> past_days_news() missing 1 required positional argument: 'past_date'

"""
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^today/$', views.news_today, name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',
        views.past_days_news, name='pastNews'),
]

"""
Once we define our URLconf for our news app we need to connect it
to our project.
"""
