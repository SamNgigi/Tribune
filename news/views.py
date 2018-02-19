# from django.shortcuts import render
"""
The HttpResponse is a class of the django.http module that is
responsible for returning a response to the user
"""
from django.http import HttpResponse
import datetime as dt

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


"""
We create another view to display the date for our news.
We import datetime module at the top.
"""


def news_of_day(request):
    date = dt.date.today()
    """
    We want to get the exact day name. We use our convert_date function
    """
    day = convert_dates(date)
    html = f'''
            <html>
                <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
                </body>
            </html>
            '''
    return HttpResponse(html)


"""
Below view function to know which day of the week it is.
"""


def convert_dates(dates):
    """
    Function that gets the week-day number for the date.
    I think the day_number returns a number between 0 and 6
    corresponding to the day of the week
    """
    day_number = dt.date.weekday(dates)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Returning the actual day of the week
    day = days[day_number]

    return day
