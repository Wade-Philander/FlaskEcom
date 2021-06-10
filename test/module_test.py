from unittest import TestCase
from market import bcrypt
from market.models import User, Item

class TestAllModels(TestCase):

    def test_users(self):
        new_user = User(username='wade', email_address='wade@gmail.com', password_hash='wade', budget=100)

        self.assertEqual(new_user.username, 'wade')
        self.assertEqual(new_user.email_address, 'wade@gmail.com')
        self.assertEqual(new_user.password_hash, 'wade')
        self.assertEqual(new_user.budget, 100)

    def test_items(self):
        new_item = Item(name='test', price=5000, barcode='123456789', description='test data')

        self.assertEqual(new_item.name, 'test')
        self.assertEqual(new_item.price, 5000)
        self.assertEqual(new_item.barcode, '123456789')
        self.assertEqual(new_item.description, 'test data')

    def test_prettier_bugdet(self):
        new_user = User(username='wade', email_address='wade@gmail.com', password_hash='wade', budget=1000).prettier_budget
        
        self.assertEqual(new_user, '1,000$')


    
    def test_generate_password(self):
        new_user = User(username='wade', email_address='wade@gmail.com', password_hash='wade', budget=1000)
        
        my_pass = bcrypt.generate_password_hash('wade')

        self.assertTrue(my_pass)

    def test_check_pass(self):
        new_user = User(username='wade', email_address='wade@gmail.com', password_hash='wade', budget=1000)

        
        pass