import factory
from api.models import User, CompanyUser
from api.tests.factories.company import CompanyFactory


class UserFactory(factory.django.DjangoModelFactory):
    """Creates an instance of the User model"""
    class Meta:
        model = User
        django_get_or_create = ('email',)
    
    first_name = 'testname'
    last_name = 'testlast'
    email = 'testemail@test.com'
    password = factory.PostGenerationMethodCall('set_password', 'anypassword')


class AdminUserFactory(factory.django.DjangoModelFactory):
    """Creates an instance of the Admin User Model"""
    class Meta:
        model = User
        django_get_or_create = ('email',)
    
    first_name = 'testadmin'
    last_name = 'testlastadmin'
    email = 'testadmin@test.com'
    password = factory.PostGenerationMethodCall('set_password', 'anypassword')
    is_staff = True
    is_superuser = True
    
class CompanyUserFactory(factory.django.DjangoModelFactory):
    """
        Creates an instance of the Company user model
    """
    class Meta:
        model = CompanyUser
        
    first_name = 'testname'
    last_name = 'testlast'
    email = 'testemail@test.com'
    password = factory.PostGenerationMethodCall('set_password', 'anypassword')
    added_by = factory.SubFactory(UserFactory)
    company = factory.SubFactory(CompanyFactory)

