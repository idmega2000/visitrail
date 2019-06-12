import factory
from api.models import User, UserProfile
from api.tests.factories.company import CompanyFactory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)
    
    first_name = 'testname'
    last_name = 'testlast'
    email = 'testemail@test.com'
    password = 'anypassword'


class AdminUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)
    
    first_name = 'testadmin'
    last_name = 'testlastadmin'
    email = 'testadmin@test.com'
    password = 'anypassword'
    is_staff = True
    is_superuser = True
    

class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    image_url = 'anyimage.com'
    company = factory.SubFactory(CompanyFactory)
