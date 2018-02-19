"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

"""
When connecting our news app to our project we add 'include' as an import.
'include' allows us to reference another URLconf.

We call the url function to our news app and create a new regex and
call the include function and pass in our news app.

Note
- In this regex we have no endstring match but a /.
This is because when Django encounters the 'include' function it
chops off whatever part of the url that matched till that point and
sends the rest to the referenced URLconf.

"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls'))
]
