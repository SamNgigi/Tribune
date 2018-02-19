from django.shortcuts import render, redirect
"""
The HttpResponse is a class of the django.http module that is
responsible for returning a response to the user
"""
from django.http import HttpResponse, Http404
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
    # return HttpResponse('Welcome to Moringa Tribune')
    return render(request, 'welcome.html')


"""
We create another view to display the date for our news.
We import datetime module at the top.
"""


def news_today(request):
    date = dt.date.today()
    """
    We want to get the exact day name. We use our convert_date function
    """

    return render(request, 'all-news/today-news.html', {"date": date, })


"""
Below view function to know which day of the week it is.
"""


def convert_dates(dates):
    """
    Function that gets the week-day number for the date.
    I think the day_number returns a number between 0 and 6
    corresponding to the day of the week

    Got and IndexError (list index out of range) because i didn't
    have Saturday and Sunday in my days list.
    """
    day_number = dt.date.weekday(dates)
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]

    return day


"""
Below we define the view function to display news from a past date.
"""


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-news/past-news.html', {"date": date})
