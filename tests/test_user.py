import unittest
from app.models import User

class UserModelTest(unittest.Testcase):
    
    def setUp(self):
        self.new_user = User(password = 'ombati')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    #second test
    def test_no_access_password(self):
        with self.assertRaise(AttributeError):
            self.new_user.password
            
            
     #third test to confirm that our password_hash can be verified       
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('ombati'))