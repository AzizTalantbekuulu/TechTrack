from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import CustomUser, Equipment

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpass', role='admin')
        self.client.login(username='admin', password='adminpass')

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'password': 'testpass', 'role': 'user'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class EquipmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='user', password='userpass', role='user')
        self.client.force_authenticate(user=self.user)

    def test_create_equipment(self):
        url = reverse('equipment-list')
        data = {'type': 'Robot', 'model': 'R2000', 'installation_date': '2021-01-01', 'status': 'active'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
