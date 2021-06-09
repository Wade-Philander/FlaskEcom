from unittest import TestCase
from run import app
from market import db

class BaseTest(TestCase):
    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['WTF_CSRF_ENABLED'] = False
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()

        def tearDown(self):
            with app.app_context():
                db.session.remove()
                db.drop_all