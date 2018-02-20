"""
Django provides a test module django.test where we import the TestCase class.

We then import our models
"""
from django.test import TestCase
from . models import Editor, Articles, Tags
# Create your tests here.


class EditorTestClass(TestCase):
    # Set up method. Make sure to spell setUp correctly
    def setUp(self):
        self.test = Editor(first_name='Test',
                           last_name='Case', email='test@gmail.com')

    # Testing proper instantiation
    def test_instance(self):
        self.assertTrue(isinstance(self.test, Editor))

    # Testing save method
    def test_saving(self):
        self.test.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
