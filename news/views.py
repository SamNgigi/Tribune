# from django.shortcuts import render
"""
The HttpResponse is a class of the django.http module that is
responsible for returning a response to the user
"""
from django.http import HttpResponse

# Create your views here.

"""
We define the function that will render our welcome message to the templates.

This function takes in the argument 'request'.

This argument contains the information of the current web request
that has triggered this view and is an instance of the
'django.http.HttpRequest' class.

This means that request is an parameter that passes in a request
object as an argument.


"""


def welcome(request):
    return HttpResponse('Welcome to Moringa Tribune')
