from api.models import CompanyUser
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
class CustomBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, company=None, **kwargs):
        try:
            user = CompanyUser.objects.get(email=email, company=company)
        except CompanyUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self,user_id):
        try:
            return CompanyUser.objects.get(pk=user_id)
        except CompanyUser.DoesNotExist:
            return None
