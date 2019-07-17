from django.test.client import Client
client = Client()
class LoginToken:
    
    def setUp(self):
        self.new_user = UserFactory()
        
    def first_token(self):
        user = {
                "email": "testemail@test.com",
                "password": "anypassword"
            }
        response = client.post('/api/v1/login', user)
        tok = dict(response.data)
        token = tok['data']['access']
        return token
