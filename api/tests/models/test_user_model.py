
from django.test import TestCase

from ..factories.user import UserFactory, AdminUserFactory, CompanyUserFactory

from ..factories.company import CompanyFactory


class TestUserModel(TestCase):
    def setUp(self):
        self.new_user = UserFactory()
        self.admin_user = AdminUserFactory()

    def test_user_model(self):
        """test instance of user model is saved in db"""

        new_user = self.new_user
        assert new_user.first_name == 'testname'
        assert new_user.last_name == 'testlast'
        assert new_user.email == 'testemail@test.com'

    def test_admin_model(self):
        """test instance of admin user model is saved in db"""

        admin_user = self.admin_user
        assert admin_user.first_name == 'testadmin'
        assert admin_user.last_name == 'testlastadmin'
        assert admin_user.email == 'testadmin@test.com'
        assert admin_user.is_staff == True
        assert admin_user.is_superuser == True

    def test_get_short_name(self):
        """test ability to get short name of user"""

        new_user = self.new_user
        assert new_user.get_short_name() == new_user.first_name
    
    def test_get_full_name(self):
        """test ability to get full name of user"""

        new_user = self.new_user
        full_name = '%s %s' % (new_user.first_name, new_user.last_name)
        
        assert new_user.get_full_name() == full_name.strip()

    def test_superuser_return(self):
        """test superuser have access to user data"""
        
        new_user = self.new_user
        assert new_user.__str__() == new_user.email


class TestCompanyUser(TestCase):
    
    def setUp(self):
        self.company_user = CompanyUserFactory()

    def test_company_user_model():

        company_user = self.company_user
        assert company_user.first_name == 'testname'
        assert company_user.last_name == 'testlast'
        assert company_user.email == 'testemail@test.com'

    def test_superuser_return(self):
        """test superuser have access to user data"""
        
        company_user = self.company_user
        assert company_user.__str__() == company_user.email

    def test_get_short_name(self):
        """test ability to get short name of user"""

        company_user = self.company_user
        assert company_user.get_short_name() == company_user.first_name
    
    def test_get_full_name(self):
        """test ability to get full name of user"""

        company_user = self.company_user
        full_name = '%s %s' % (company_user.first_name, company_user.last_name)
        
        assert company_user.get_full_name() == full_name.strip()
