"""
We import the models class from the 'django.db' modules.

A models is basically a python class that inherits from the
'modules.Model' class
"""
from django.db import models

# Create your models here.


class Editor(models.Model):
    """
    We create the Editor class that inherits from the modules.

    We then create three classs variables that represent different
    columns in our database.

    We use Field objects to define what sort of data the database will store.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    """
    We add an __str__ function that will return a string
    representation of our model.

    This will be useful  when we watn to view our returned queries
    """

    def __str__(self):
        return self.first_name

    # The save method
    def save_editor(self):
        self.save()

    """
    Changed
    ordering = ['name']
    to
    ordering = ['first_name'],

    Removed below error
        SystemCheckError: System check identified some issues:
        ERRORS:
        news.Editor: (models.E015) 'ordering' refers to the
        non-existent field 'name'.
    """
    class Meta:
        ordering = ['first_name']


class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # The save method
    def save_tag(self):
        self.save()


class Articles(models.Model):
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
    body = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    # The save method
    def save_article(self):
        self.save()

    # The delete method
    def delete_article(self):
        self.delete()
