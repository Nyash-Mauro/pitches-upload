	import unittest
from app.models import Pitch, User, Comments
from datetime import datetime
from app import db
class PitchTest(unittest.TestCase):
    
   def setUp(self):
    self.user_Me = User(username = 'Me', password = 'Herme', email = 'her@gmail.com')
    self.new_pitch = Pitch(title = 'test', content = 'hire me',user_id = 1, category = 'interview')
def tearDown(self):
    Pitch.query.delete()
    User.query.delete()
def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.title, 'test')
    self.assertEquals(self.new_pitch.content, 'hire me' )
    self.assertEquals(self.new_pitch.user_id, 1)
    self.assertEquals(self.new_pitch.category, 'interview')
    def test_save_pitch(self):
     self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)
