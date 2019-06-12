from django.db import models

from .base import BaseModel

# Create your models here.

class Company(BaseModel):
    """ Model that hold the company data """

    company_name = models.CharField(max_length=100)
    industry_type = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    added_by = models.ForeignKey('api.User', null=True, on_delete=models.SET_NULL)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.company_name

class CompanyCenter(BaseModel):
    """ Model that hold the company centers """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    center = models.CharField(max_length=30)

    def __str__(self):
        return self.center
