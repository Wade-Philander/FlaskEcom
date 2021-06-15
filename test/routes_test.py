from test.base_test import BaseTest, db

class TestRoute(BaseTest):
    def test_home(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/home')
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Welcome to Jim Shaped Coding Market', response.data)

    def test_register(self):
        with self.app:
            response = self.app.get('/register')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/register', response.get_data())

    def test_login(self):
        with self.app:
            response = self.app.get('/login')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'/login', response.get_data())

    def test_logout(self):
        with self.app:
            response = self.app.get('/logout')
            self.assertEqual(response.status_code, 302)