from django.test import TestCase
from .models import BookCatalogue

class BookCatalogueTestCase(TestCase):
    
    def setUp(self):
        BookCatalogue.objects.create('tcuser1@work.com','Learning Django Web Development','Sanjeev Jaiswal',)
