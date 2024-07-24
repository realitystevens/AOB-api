from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
import random, string



INVALID_APITOKEN = ''.join(random.choices(string.ascii_letters.lower() + string.digits, k=25))

class APITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='!@nimda()')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token f{self.token.key}')
    
    # def test_api_access(self):
    #     response = self.client.get('/api/products/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_access(self):
        self.client.credentials()  # Remove token
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token f{INVALID_APITOKEN}')
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
