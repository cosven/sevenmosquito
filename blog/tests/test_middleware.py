from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class TestSetBloggerByHostMiddleware(TestCase):

    def setUp(self):
        self.client = Client()

    def test_1(self):
        resp = self.client.get(reverse('blog:check_health'), HTTP_HOST='yannnli.me')
        self.assertEqual(resp.status_code, 200)

    def test_2(self):
        resp = self.client.get(reverse('blog:check_health'))
        self.assertEqual(resp.status_code, 400)
