from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
"""
The HttpResponse is a class of the django.http module that is
responsible for returning a response to the user
"""
from django.http import Http404, JsonResponse
from .models import Article, NewsLetterRecipients, MoringaMerch
from .forms import NewsLetterForm, NewsArticleForm
from .email import send_welcome_email
import datetime as dt

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import MerchSerializer

from .permissions import IsAdminorReadOnly

# Create your views here.


class MerchList(APIView):
    permission_class = (IsAdminorReadOnly,)

    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Merch Description
# Working properly


class MerchDescription(APIView):
    permission_classes = (IsAdminorReadOnly,)

    def get_merch(self, pk):
        try:
            return MoringaMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


def news_today(request):
    """
    We call our 'todays_news' function that returns news aricles
    published today.
    """
    date = dt.date.today()
    news_zote = Article.all()
    news = Article.todays_news()
    form = NewsLetterForm()
    return render(request, 'all-news/todays-news.html',
                  {"date": date,
                   "news": news,
                   "form": form,
                   "news_zote": news_zote})


"""
Below we define the view function to display news from a past date.
"""


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {
        'success': 'You have been successfully added to the mailing list.'
    }
    return JsonResponse(data)


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


@login_required(login_url='/accounts/login/')
def article(request, article_id):
    article = Article.objects.get(id=article_id)

    return render(request, 'all-news/article.html', {"article": article})


def search_results(request):
    """
    This function defines our search results view.

    We first check if the article query exists in our request.GET object
    and then check if it has a value.

    We then get the search term using the get method called on the
    request.GET object.

    Next we call the search_by_title method class method we created in
    our models and pass in the user input.

    We then render a HTML template and pass in the list of articles found
    by our method and the search_term itself
    """
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',
                      {"message": message, "articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
    else:
        form = NewsArticleForm()
    return render(request, 'new-article.html', {"form": form})
