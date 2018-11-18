from django.test import TestCase
from django.db.utils import IntegrityError

from store.models import Store

class StoreTest(TestCase):

    def test_create_one_book_for_store(self):
        book = Store.objects.create(name='Test name')
        self.assertEqual(Store.objects.count(), 1)

    def test_if_possible_to_see_name_of_book(self):
        book = Store.objects.create(name='Test name')
        self.assertEqual(Store.objects.first().name, 'Test name')

    def test_create_two_books_for_store(self):
        Store.objects.create(name='Book one')
        Store.objects.create(name='Book two')

    def test_book_have_property_name_called_hsh_with_128_caracters(self):
        book = Store.objects.create(name='Book')
        self.assertEqual(len(Store.objects.first().hsh), 128)
        
    def test_book_hsh_its_unique(self):
        book = Store.objects.create(name='Book')
        other_book = Store()
        other_book.name = 'Other Book'
        other_book.hsh = book.hsh
        with self.assertRaises(IntegrityError):
            other_book.save()   
