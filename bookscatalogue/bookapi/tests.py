from django.test import TestCase
from .models import BookCatalogue
from rest_framework.test import APIRequestFactory
class BookAPITestCase(APIRequestFactory):
    # Test cases for APIs
    def test_get(self):
        response = self.get('/books/v1/books/')
        self.assert response.status_code == 200
    
    def test_post(self):
        response = self.post('/books/v1/books/',{
                'email':'tcuser2@work.com',
                'title':'Learning Django Web Development',
                'author':'Sanjeev Jaiswal',
                'date_added':'',
                'isbn':'9781783983704'
                }
            )
        self.assert response.status_code == 200

    def test_put(self):
        response = self.post('/books/v1/books/1/',{
                'date_added':'2020-09-12',
                }
            )
        self.assert response.status_code == 200

    def test_delete(self):
        response = self.delete('/books/v1/books/1/')
        self.assert response.status_code == 200

class BookCatalogueTestCase(APITestCase):
    
    def setUp(self):
        BookCatalogue.objects.create('tcuser1@work.com','Learning Django Web Development','Sanjeev Jaiswal','2020-10-01','9781783983704')

    def test_book_added(self):
        pass

    def test_valid_isbn(self):
        pass
