from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

# Create your tests here.

class UserRegistrationTest(APITestCase):
    def test_registration(self):  #회원가입 테스트
        url = reverse("user_view")   # url name
        user_data = {
            "username": "testuser",
            "fullname": "테스터",
            "email": "test@test.com",
            "password":"1234",
        }
        response = self.client.post(url, user_data)  # APITestCase의 기본적인 세팅
        self.assertEqual(response.data["message"], "가입 완료!!")