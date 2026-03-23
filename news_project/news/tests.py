from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser


class ArticleTests(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.reader = CustomUser.objects.create_user(
            username="reader",
            password="123",
            role="reader"
        )

        self.journalist = CustomUser.objects.create_user(
            username="journalist",
            password="123",
            role="journalist"
        )


    def test_reader_login(self):

        response = self.client.post(
            "/api/token/",
            {
                "username": "reader",
                "password": "123"
            }
        )

        self.assertEqual(response.status_code, 200)