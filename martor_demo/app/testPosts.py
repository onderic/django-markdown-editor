from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def test_post_creation(self):
        post = Post(title="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "My Title", "Title is not set correctly")
        self.assertEqual(post.description, "Blurb", "Description is not set correctly")
        self.assertEqual(post.wiki, "Post Body", "Wiki is not set correctly")
