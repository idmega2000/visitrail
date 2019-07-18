from django.test import TestCase

from ..factories.visitor import VisitorFactory
from ..factories.user import UserFactory


class TestVisitorModel(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.new_visitor = VisitorFactory.create(host=self.user)

    def test_visitor_model(self):
        """test instance of visitor model is saved in db"""
        new_visitor = self.new_visitor
        assert new_visitor.host == self.user
        assert new_visitor.first_name == 'test'
        assert new_visitor.last_name == 'testlast'
        assert new_visitor.phone == '00000000'
        assert new_visitor.visit_location == 'world'
        assert new_visitor.visit_start_period == '2019-06-10 00:22:32'
        assert new_visitor.visit_end_period == '2019-06-10 00:32:32'
        assert new_visitor.__str__() == new_visitor.first_name
        
