from django.test import TestCase

from store.models import Store

class StoreTest(TestCase):

    def test_create_one_book_for_store(self):
        book = Store.objects.create(name='Test name')
        self.assertEqual(Store.objects.count(), 1)
