from django.test import TestCase
from django.db.utils import IntegrityError

from store.models import Store

class StoreTest(TestCase):

    def test_if_possible_to_see_name_of_book(self):
        book = Store.objects.create(name='Test name', pages=1)
        self.assertEqual(Store.objects.first().name, 'Test name')

    def test_create_two_books_for_store(self):
        Store.objects.create(name='Book one', pages=1)
        Store.objects.create(name='Book two', pages=2)
        self.assertEqual(Store.objects.count(), 2)

    def test_book_have_property_name_called_hsh_with_128_caracters(self):
        book = Store.objects.create(name='Book', pages=1)
        self.assertEqual(len(Store.objects.first().hsh), 128)
        
    def test_book_hsh_its_unique(self):
        book = Store.objects.create(name='Book', pages=1)
        other_book = Store()
        other_book.name = 'Other Book'
        other_book.hsh = book.hsh
        other_book.pages = 1
        with self.assertRaises(IntegrityError):
            other_book.save()   

    def test_book_name_its_unique(self):
        book = Store.objects.create(name='Book', pages=1)
        with self.assertRaises(IntegrityError):
            other_book = Store.objects.create(name='Book', pages=1)

    def test_create_book_only_with_name_and_pages(self):
        book = Store.objects.create(name='Book', pages=1)
        self.assertEqual(Store.objects.count(), 1)

    def test_not_create_book_without_page(self):
        with self.assertRaises(IntegrityError):
            Store.objects.create(name='Book')
