import unittest
from app.models import Blog

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(id = 1, title = 'hilarious', post = 'I saw you in my dreams and i dint wanna wake up', upvote = 1, downvote = 1, author = 'james')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))
