import unittest
from app.models import User, Pitch, Comments
from app import db
from datetime import datetime

class TestModelComment(unittest.TestCase):
  def setUp(self):
    self.user_her = User(username = 'her', password='Herme', email='her@gmail.com')
    self.new_pitch = Pitch(title = 'test', content = 'hire me',user_id = 1, category = 'interview')
    self.new_comment = Comments(id = 1, comment = 'test', user_id = 1, pitch = self.new_pitch)
    def tearDown(self):
       Pitch.query.delete()
    User.query.delete()
    def test_instance_variables(self):
      self.assertEquals(self.new_comment.id, 1)
    self.assertEquals(self.new_comment.comment, 'test')
    self.assertEquals(self.new_comment.user_id, 1)
def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all()),1)
def test_save_multiple_comment(self):
    self.new_comment.save_comment()
    self.second_her = User(username = 'me', password='Herme', email='me@gmail.com')
    self.second_pitch = Pitch(title = 'test', content = 'hire',user_id = 2, category = 'interview')
    self.second_comment = Comments(id = 2, comment = 'test', user_id = 2, pitch = self.new_pitch)
    self.secpnd_comment.save_comment()
    self.assertTrue(len(Comments.query.all()),2)