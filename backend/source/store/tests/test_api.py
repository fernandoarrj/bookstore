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

    def test_can_PUT_a_book_register(self):
         

