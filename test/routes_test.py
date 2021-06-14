from test.base_test import BaseTest, db
from market.models import User, Item
from flask import request
from flask_login import current_user, AnonymousUserMixin


class HomeTest(BaseTest):
    
    def test_route(self):
        with self.app:
            response = self.app.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_route_home(self):
        with self.app:
            response = self.app.get('/home', follow_redirects=True)
            self.assertIn('/home', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jim Shaped Coding Market', response.data)
    
class TestLogin(BaseTest):
    def test_login_route(self):
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            self.assertIn('/login', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)
    def test_route_market(self):
        with self.app:
            response = self.app.get('/market', follow_redirects=True)
            # self.assertIn('/market', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)
            
            
class TestRegister(BaseTest):
    def test_register_route(self):
        with self.app:
            response = self.app.get('/register', follow_redirects=True)
            self.assertIn('/register', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Create your Account', response.data)
            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))
 

class TestLogin(BaseTest):
    def test_login_route(self):
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            self.assertIn('/login', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)