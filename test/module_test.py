from unittest import TestCase
from market import bcrypt
from market.models import User, Item
from test.base_test import BaseTest, db

class TestAllModels(BaseTest):

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


# MAKE THIS AN INTEGRATION TEST
    # def test_check_password_correction(self):
    #     new_user = User(username='wade', email_address='wade@gmail.com', password_hash='wadeb', budget=1000)
    #     print(new_user.password_hash)

    #     #password = bcrypt.generate_password_hash(new_user)
    #     #new_pass = bcrypt.check_password_hash(password, 'wadeb')#
    #     #self.assertTrue(new_pass)
    #     #print(password)

        

    def test_password_setter(self):
            password = 'qwerty'
            pw_hash = bcrypt.generate_password_hash(password)
            self.assertTrue(pw_hash)
        
        
    def test_passw_verification(self):
        
        password = 'qwerty'
        pw_hash = bcrypt.generate_password_hash(password)
        ps_hash = bcrypt.check_password_hash(pw_hash, 'qwerty')
        self.assertTrue(ps_hash)
        
    def test_purchase(self):
        user = User(username='qwert', email_address='test@gmail.com', password_hash='passwords', budget=2000).can_purchase(Item(
        name='paper', price=1000, barcode='white', description='test'  
        ))
        self.assertTrue(user)    
        
    
            
    def test_item(self):
        item = Item(name='paper', price=15, barcode='white', description='test')
        
        self.assertEqual(item.name, 'paper', "this the name")
        self.assertEqual(item.price, 15)
        self.assertEqual(item.barcode, 'white')
        self.assertEqual(item.description, 'test')

    def test_repr(self):
        item = Item(name='car', price=15, barcode='white', description='test')
        
        self.assertEqual(item.__repr__(), "Item car")

    def test_sell_method(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register', data=dict(
                    username='kevin', email_address='okay1@gmail.com',
                    password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(username='kevin').first()
                self.assertTrue(user)
                
                response1 = self.app.post('/register', data=dict(
                    username='carl', email_address='okay2@gmail.com',
                    password1='password', password2='password'), follow_redirects=True)
                user1 = db.session.query(User).filter_by(username='carl').first()
                self.assertTrue(user1)
                
                
                item = Item(id=1, name="vans", price=2000, barcode=123456, description="white", owner=1)
                db.session.add(item)
                db.session.commit()
                
                items = db.session.query(Item).filter_by(name="vans")

                
                self.assertTrue(items)

                
                self.assertTrue(user.can_sell(item_obj=item))

                    
                self.assertFalse(user1.can_sell(item_obj=item))