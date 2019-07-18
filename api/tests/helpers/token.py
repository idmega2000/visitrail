from django.test.client import Client
client = Client()
class LoginToken:
    """Generates the login credentials"""
    def setUp(self):
        self.new_user = UserFactory()
        
    def first_token(self):
        """Generates the login login token and credentials for first user"""
        user = {
                "email": "testemail@test.com",
                "password": "anypassword"
            }
        response = client.post('/api/v1/login', user)
        tok = dict(response.data)
        token = tok['data']['access']
        return token
