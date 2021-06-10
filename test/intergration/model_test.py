from typing import NewType
from test import BaseTest, db
from market.models import Item, User


class TestAllModel(BaseTest):
    
    #test that user can be saved and deleted
    def test_user_crud(self):
        with self.app_context():
            new_user = User(data = 'New user')
            #assert that this user user does not exist
            results = db.session.query(User).filter_by(data='New user').first()
            self.assertIsNone(results)
            #save user to db
            db.session.add(new_user)
            db.session.commit()
            #delete user from db
            db.session.delete(new_user)
    #test if item gets saved 
    def test_item_crud(self):
        with self.app_context():
            new_item = Item(data = 'New Item')
            result = db.session.query(Item).filter_by(data='New Item').first()
            self.assertIsNone(result)
            db.session.add(new_item)
            db.session.commit()
            