
from ..factories.user import UserFactory, AdminUserFactory

from ..factories.company import CompanyFactory
from rest_framework.test import APITestCase
from ..helpers.token import LoginToken

class TestUserAuth(APITestCase):
    """Tests for the user API view."""

    def setUp(self):
        self.new_user = UserFactory()

    def test_signup_single_user_with_bad_password_fails(self):
        """Test getting information of a user who is in the database."""
        user = {
            "email": "testemail1@test.com",
            "last_name": "testlast",
            "first_name": "walex",
            "password": "dkd"
        }
        response = self.client.post('/api/v1/signup', user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['status'], 'error')

    def test_signup_single_user_successfully(self):
        """Test user signup successfully"""
        user = {
            "email": "testemail1@test.com",
            "last_name": "testlast",
            "first_name": "walex",
            "password": "anypassword"
        }
        response = self.client.post('/api/v1/signup', user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 'success')
    
    def test_user_login_with_bad_credentials_fails(self):
        """Test user login with bad credentials"""
        user = {
            "email": "testemail@test.com",
            "password": "anyssword"
        }
        response = self.client.post('/api/v1/login', user)
        self.assertEqual(response.status_code, 401)

    def test_user_login_successful(self):
        """Test user login successfull"""
        user = {
            "email": "testemail@test.com",
            "password": "anypassword"
        }
        response = self.client.post('/api/v1/login', user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['email'], user['email'])


class TestUser(APITestCase):

    def setUp(self):
        self.new_user = UserFactory()
        self.new_token = LoginToken().first_token()

    def test_user_list_without_token(self):
        """Test get all user without authentication"""
        response = self.client.get('/api/v1/user')

        self.assertEqual(response.status_code, 401)

    def test_user_list(self):
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.new_token
        }
        response = self.client.get('/api/v1/user', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data'][0]['email'], 'testemail@test.com')
        self.assertEqual(response.data['data'][0]['last_name'], 'testlast')
        self.assertEqual(response.data['data'][0]['first_name'], 'testname')

    def test_get_user_data_without_token(self):
        """Test get a user without authentication"""
        user_id = self.new_user.id
        url = f'/api/v1/user/{user_id}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)

    def test_get_a_user(self):
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.new_token
        }
        user_id = self.new_user.id
        url = f'/api/v1/user/{user_id}'
        response = self.client.get(url, **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['email'], 'testemail@test.com')
        self.assertEqual(response.data['data']['last_name'], 'testlast')
        self.assertEqual(response.data['data']['first_name'], 'testname')
    
    def test_edit_user_data_without_token(self):
        """Test edit user without authentication"""
        user_id = self.new_user.id
        url = f'/api/v1/user/{user_id}'

        user = {
            "email": "testemail1@test.com",
            "last_name": "testlast",
            "first_name": "walex",
            "password": "anypassword"
        }
        response = self.client.put(url, user)

        self.assertEqual(response.status_code, 401)

    def test_edit_a_user_data_fails(self):
        """Test edit user that is not you"""
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.new_token
        }
        user = {
            "email": "testemail1@test.com",
            "last_name": "testlast",
            "first_name": "walex",
            "password": "anypassword"
        }

        user_id = self.new_user.id
        url = f'/api/v1/user/dhjkshkdjhkdsjh'
        response = self.client.get(url, user, **headers)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['error'], 'unauthorized')
        self.assertEqual(response.data['message'], 'Attempted to alter another user\'s record(s)')


    def test_edit_a_user_data_succeeds(self):
        """Test edit a user"""
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.new_token
        }
        user = {
            "email": "testmail1@test.com",
            "last_name": "testlast",
            "first_name": "walex",
            "password": "anypassword"
        }

        user_id = self.new_user.id
        url = f'/api/v1/user/{user_id}'
        response = self.client.get(url, user, **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['email'], 'testemail@test.com')
        self.assertEqual(response.data['data']['last_name'], 'testlast')
        self.assertEqual(response.data['data']['first_name'], 'testname')
