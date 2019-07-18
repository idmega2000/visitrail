import factory
from api.models import Company, CompanyCenter, User


class UserFactory(factory.django.DjangoModelFactory):
    """Creates an instance of the User Model"""
    class Meta:
        model = User
        django_get_or_create = ('email',)
    
    first_name = 'testname'
    last_name = 'testlast'
    email = 'testemail@test.com'
    password = 'anypassword'

class CompanyFactory(factory.django.DjangoModelFactory):
    """Creates an instance of the Company model"""

    class Meta:
        model = Company

    company_name = 'testname'
    industry_type = 'information'
    phone = '909090'
    address = 'any address'
    added_date = '2019-06-10 00:22:32'
    added_by = factory.SubFactory(UserFactory)

    

class CompnayCenterFactory(factory.django.DjangoModelFactory):
    """Creates an instance of the Company Center model"""

    class Meta:
        model = CompanyCenter
    
    company = factory.SubFactory(CompanyFactory)
    center = 'anywhere'

