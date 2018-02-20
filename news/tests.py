"""
Django provides a test module django.test where we import the TestCase class.

We then import our models
"""
from django.test import TestCase
from . models import Editor, Articles, Tags
# Create your tests here.


class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test = Editor(first_name='Test',
                           last_name='Case', email='test@gmail.com')

    # Testing proper instantiation
    def test_instance(self):
        self.assertTrue(isinstance(self.test, Editor))
