import factory
from api.models import Visitor
from ..factories.user import UserFactory

class VisitorFactory(factory.DjangoModelFactory):
    """Creates an instance of the Visitor"""

    class Meta:
        model = Visitor

    host = factory.SubFactory(UserFactory)
    first_name = 'test'
    last_name = 'testlast'
    email = 'test@test.com'
    phone = '00000000'
    visit_start_period = '2019-06-10 00:22:32'
    visit_end_period = '2019-06-10 00:32:32'
    visit_location = 'world'
