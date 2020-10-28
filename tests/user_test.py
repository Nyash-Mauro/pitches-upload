import unittest
from app.models import User

class test_userModel(unittest.TestCase):
    # to test behaivours in the user model

 def setUp(self):
    self.new_user = User(password='mypassword')

def test_setPassword(self):
    # to test if there is a password
    self.assertTrue(self.new_user.secure_pass is not None)

def test_check_password(self):
    self.assertTrue(self.new_user.check_password('mypassword'))
