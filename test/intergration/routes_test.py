from test.base_test import BaseTest, db
from market.models import User, Item
from flask import request
from flask_login import current_user, AnonymousUserMixin 
from flask import request
from market.routes import register_page,
# from market.__init__ import db
from market.__init__ import db, app


class TestForms(BaseTest):
# testing register route post(sucessful register)
    def test_register_username(self):
        with self.app:
            with self.app_context():
                # correct details
                response = self.app.post('/register', data=dict(username='test', email_address='test@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test', response.data)
                self.assertEqual(current_user.get_id(), '1')
    
    def test_login(self):
        with self.app:
            with self.app_context():
                response = self.app.post('/register', data=dict(username='test2', email_address='test2@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test2@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test2', response.data)
                self.assertEqual(current_user.get_id(), '1')
                
                response = self.app.post('/login', data=dict(username='test2', email_address='test2@test.com', password='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(username='test2').first()
                self.assertTrue(user)
                self.assertIn(b'Success! You are logged in as: test2', response.data)
    
    def test_logout(self):
        with self.app:
            with self.app_context():
                response = self.app.post('/register', data=dict(username='test3', email_address='test3@test.com', password1='password', password2='password'), follow_redirects=True)
                user = db.session.query(User).filter_by(email_address='test3@test.com').first()
                self.assertTrue(user)
                self.assertIn(b'Account created successfully! You are now logged in as test3', response.data)
                self.assertEqual(current_user.get_id(), '3')
                
                response = self.app.post('/login', data=dict(username='test3', email_address='test3@test.com', password='password'), follow_redirects=True)
                self.assertTrue(user)
            
                response = self.app.get('/log-out', follow_redirects=True)
                self.assertEqual(response.status_code, 200)
        
                self.assertIn('/log-in', request.url)
                self.assertFalse(current_user.is_active)
    
    def test_market(self):
        with self.app:
            with self.app_context():
                # create user n login
                response = self.app.post('/register', data=dict(username='test4', email_address='test3@test.com', password1='password', password2='password'), follow_redirects=True)
                self.assertEqual(current_user.get_id(), '1')
                user = db.session.query(User).filter_by(username='test4').first()
                user.budget = 7000
                db.session.commit()
                # check if user budget is 7000
                self.assertEqual(user.budget, 7000)
                
                # create item save to db
                item = Item(name='fish rod', price=1200, barcode='123456789', description='description')
                db.session.add(item)
                db.session.commit()
                result = db.session.query(Item).filter_by(name="fish rod").first()
                self.assertTrue(result)
                
                # buy item in market
                response = self.app.post('/market',data=dict(purchased_item='fish rod') ,follow_redirects=True)

                self.assertIn(b'You purchased fish rod for 1200$', response.data)

    #sell item
                
    def test_sell_item(self):
        with self.app:
            self.app.post('/register', data=dict(username='test', email_address='test@gmail.com', password1='testing',
                                                 password2='testing'),
                          follow_redirects=True)

            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            self.assertTrue(current_user.get_id(), '1')

            user = db.session.query(User).filter_by(username='test').first()
            self.assertEqual(user.username, 'test')

            item = Item(id=1, name='Phone', price=100, barcode='123456789', description='describe')

            db.session.add(item)
            db.session.commit()

            self.assertEqual(user.items, [])

            response = self.app.post('/market', data=dict(sold_item='Phone'), follow_redirects=True)

            self.assertIn(b'Error', response.data)
