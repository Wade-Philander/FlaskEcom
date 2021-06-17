from flask import request
from flask_login import current_user, AnonymousUserMixin
from market.forms import RegisterForm
from wtforms.validators import ValidationError
from test.base_test import BaseTest, db
from market.models import User

class TestRegister(BaseTest):
    def test_a_valid_username(self):
        with self.app:
            self.app.post('/register', data=dict(
                username='fred', email_address='fred@gmail.com',
                password1='qwerty', password2='qwerty'
            ), follow_redirects=True)
            class Username():
                data = 'jack'
            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_username(Username)
                self.assertEqual('Username already exists! Please try a', str(context.exception))
            
    def test_a_valid_email(self):
        with self.app:
            self.app.post('/register', data=dict(
                username='jack', 
                email_address='i@gmail.com',
                password1='qwerty', 
                password2='qwerty'
            ), follow_redirects=True)
            class Email():
                data = 'jack'
            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_email_address(Email)
                self.assertEqual('Email Address already exists! Please try again', str(context.exception))