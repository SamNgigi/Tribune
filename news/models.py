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
