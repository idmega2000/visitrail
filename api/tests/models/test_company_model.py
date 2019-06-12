from django.test import TestCase

from ..factories.company import CompanyFactory, CompnayCenterFactory
from ..factories.user import UserFactory


class TestCompanyModel(TestCase):
    def setUp(self):
        self.company = CompanyFactory()
        self.company_center = CompnayCenterFactory(company=self.company)

    def test_company_model(self):
        company = self.company
        assert company.company_name == 'testname'
        assert company.industry_type == 'information'
        assert company.address == 'any address'
        assert company.phone == '909090'
        assert company.added_date == '2019-06-10 00:22:32'

    def test_company_center_model(self):
        company_center = self.company_center
        assert company_center.company == self.company
        assert company_center.center == 'anywhere'


    def test_superuser_company_return(self):
        company = self.company
        assert company.__str__() == company.company_name

    def test_superuser_company_center_return(self):
        company_center = self.company_center
        assert company_center.__str__() == company_center.center

