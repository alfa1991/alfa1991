# tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITests(APITestCase):
    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'Test Item', 'description': 'Test Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
