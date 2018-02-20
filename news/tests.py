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
    def test_saving_editors(self):
        self.test.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticlesTestClass(TestCase):
    # Set up method. Make sure to spell setUp correctly
    def setUp(self):
        self.test = Editor(first_name='Test',
                           last_name='Case', email='test@gmail.com')
        self.test.save_editor()

        self.test_article = Articles(title='Test Title',
                                     body='This is a test body',
                                     editor=self.test)

    # Testing proper instantiation
    def test_instance(self):
        self.assertTrue(isinstance(self.test_article, Articles))
        self.assertTrue(isinstance(self.test, Editor))

    # Testing save method
    def test_saving_articles(self):
        # self.test.save_editor()
        self.test_article.save_article()
        articles = Articles.objects.all()
        self.assertTrue(len(articles) > 0)

    def test_deleting_articles(self):
        self.test = Editor(first_name='Test',
                           last_name='Case', email='test@gmail.com')
        self.test.save_editor()
        self.test_article = Articles(title='Test Title',
                                     body='This is a test body',
                                     editor=self.test)
        self.test_article.save_article()
        # self.test.save_editor()
        self.test_article.delete_article()
        articles = Articles.objects.all()
        self.assertTrue(len(articles) < 1)


class TagsTestClass(TestCase):
    # Set up method. Make sure to spell setUp correctly
    def setUp(self):
        self.test = Editor(first_name='Test',
                           last_name='Case', email='test@gmail.com')
        self.test.save_editor()

        self.test_article = Articles(title='Test Title',
                                     body='This is a test body',
                                     editor=self.test)
        self.test_article.save_article()

        self.tag_test = Tags(name='Testing')

    # Testing proper instantiation
    def test_instance(self):
        self.assertTrue(isinstance(self.test, Editor))
        self.assertTrue(isinstance(self.test_article, Articles))
        self.assertTrue(isinstance(self.tag_test, Tags))

    # Testing save method
    def test_save_tags(self):
        # self.test.save_editor()
        self.tag_test.save_tag()
        tags = Tags.objects.all()
        self.assertTrue(len(tags) > 0)
