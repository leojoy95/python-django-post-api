from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class PostTest(TestCase):
    def setUp(self):
        # create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # create a blog post
        test_post = Post.objects.create(author=testuser1, title="A good title", body="Nice body content")
        test_post.save()

    def test_string_representation(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "A good title")
        self.assertEqual(body, "Nice body content")
