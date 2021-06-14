from test.base_test import BaseTest, db
from market.models import User, Item

class TestRoutes(BaseTest):
    def test_reg(self):
        with self.app:
            response = self.app.post('/register',data=dict(username='test', email_address='test@gmail.com', password='pass'), follow_redirects=True)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)