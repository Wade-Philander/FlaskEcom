
from test.base_test import BaseTest, db
from market.models import Item, User


class TestAllModel(BaseTest):
    
    #test that user can be saved and deleted
    def test_user_crud(self):
        with self.app:
            new_user = User(username = 'New user', email_address='newuser@gmail.com', password_hash='54efdyf465gth5gurgh6ur56gth6ru575u5y6i76t')
            #assert that this user user does not exist
            results = db.session.query(User).filter_by(username='New user').first()
            self.assertIsNone(results)
            #save user to db
            db.session.add(new_user)
            db.session.commit()
            #delete user from db
            db.session.delete(new_user)

    #test if item gets saved 
    def test_item_crud(self):
        with self.app:
            new_item = Item(name = 'New Item', price=7000, barcode='jyfjguygkui', description='new item', owner=23)
            result = db.session.query(Item).filter_by(name='New Item').first()
            self.assertIsNone(result)
            db.session.add(new_item)
            db.session.commit()
            