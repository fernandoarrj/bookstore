from django.test import TestCase
from django.db.utils import IntegrityError

from rest_framework.test import APIClient

from store.models import Store

class StoreAPITest(TestCase):
    
    def setUp(self):
        self.api_client = APIClient()
    
    def test_can_POST_a_book(self):
        data = {'name': 'Book', 'pages': 1}
        resp = self.api_client.post('/api/store/', data)

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Store.objects.count(), 1)

    def test_cant_POST_a_book_without_pages(self):
        data = {'name': 'Book'}

        with self.assertRaises(IntegrityError): 
            resp = self.api_client.post('/api/store/', data)
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(Store.objects.count(), 0)

    def test_can_PUT_a_book_register_with_hsh(self):
        book = Store.objects.create(name='Book', pages=1)
        
        data = {'name': 'Change Book', 'pages': 2}
        url = '/api/store/%s/' % (book.hsh)
        resp = self.api_client.put(url, data)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Store.objects.first().name, 'Change Book')
        self.assertEqual(Store.objects.first().pages, 2)

    def test_can_DELETE_a_book_register_with_hsh(self):
        book = Store.objects.create(name='Book', pages=1)
        
        url = '/api/store/%s/' % (book.hsh)
        resp = self.api_client.delete(url)

        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Store.objects.count(), 0)

    def test_can_GET_a_book_register_with_hsh(self):
        book = Store.objects.create(name='Book', pages=1) 
        other_book = Store.objects.create(name='Other Book', pages=2)

        url = '/api/store/%s/' % (book.hsh)
        resp = self.api_client.get(url)
    
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'Book')

    def test_can_GET_a_list_of_books(self):
        book = Store.objects.create(name='Book', pages=1)
        other_book = Store.objects.create(name='Other Book', pages=2)
        
        resp = self.api_client.get('/api/store/')
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 2)
    
        
