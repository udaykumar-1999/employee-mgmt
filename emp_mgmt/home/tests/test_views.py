from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from home.views import EmployeeViews

class EmployeeViews(APITestCase):

    def test_get_emp(self):
        resp = self.client.get('/api/employees/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    
    def test_post_emp(self):
        data = {
          "name":"mahesh",
          "age":23,
          "gender":"M",
          "department":"IT",
          "salary":50000
        }
        resp = self.client.post('/api/employees/', data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
    