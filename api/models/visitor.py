from django.db import models
from .base import BaseModel

# Create your models here.

class Visitor(BaseModel):
    """ Model that hold the visitor data """

    host = models.ForeignKey('api.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200) 
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    visit_start_period = models.DateTimeField()
    visit_end_period = models.DateTimeField()
    visit_location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name
