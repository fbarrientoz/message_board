from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    """
    docstring
    """
    def setUp(self):
        Post.objects.create(text="....")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name= f"{post.text}"
        self.assertEqual(expected_object_name, "....")

class HomePageViewTest(TestCase):
    """
    docstring
    """
    def setUp(self):
        Post.objects.create(text="....")

    def test_view_url(self):
        """
        docstring
        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


    def test_view_url_by_name(self):
        """
        docstring
        """
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        """
        docstring
        """
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')