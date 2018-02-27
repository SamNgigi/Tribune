"""
We import the models class from the 'django.db' modules.

A models is basically a python class that inherits from the
'modules.Model' class
"""
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models
import datetime as dt

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # The save method
    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()


class Article(models.Model):
    """
    Defining the Articles class.

    This model has a one to many relationship between articles and the editor.
        An article has one editor... but one editor can edit multiple articles

    This model also has a many to many relationship between articles and tags.
        -A single article can have may tags and a single tag can
        be shared by multiple articles

    To get the dates when an article was posted we add a timespamp to our model
    """
    title = models.CharField(max_length=60)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField(blank=True)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    # blank=True allows  to continue with article image as null for now.
    article_image = models.ImageField(upload_to='articles/', blank=True)

    # The save method
    def save_article(self):
        self.save()

    # The delete method
    def delete_article(self):
        self.delete()

    @classmethod
    def todays_news(cls):
        """
        We use the Django query filter date that allows us to convert
        out datetimefield to a date.

        Note the twwo underscores after the first date.
        """
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def all(cls):
        news = cls.objects.all()
        return news

    @classmethod
    def date_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        """
        This is a method that will help us fileter all the Articles in
        our database and return one matching a search query.

        This search query is passed in as search_term the second
        argument in our method.

        We use the __icontains query filter that checks if any word in
        the title field of our articles matches the search term.

        We return the result.
        """
        news = cls.objects.filter(title__icontains=search_term)
        return news


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
