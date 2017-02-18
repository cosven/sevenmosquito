from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from blog.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(name='yannnli')

    def test_index(self):
        resp = self.client.get(reverse('blog:index'), HTTP_HOST='yannnli.me')
        self.assertEqual(resp.status_code, 200)
