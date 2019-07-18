from django.db import models
from django.core.validators import MinLengthValidator

#local imports
from .base import BaseModel

class Company(BaseModel):
    """ Model that hold the company data """

    company_name = models.CharField(max_length=100)
    industry_type = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, validators=[MinLengthValidator(6)], blank=True, null=True)
    address = models.TextField()
    added_by = models.ForeignKey('api.User', null=True, on_delete=models.SET_NULL)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class CompanyCenter(BaseModel):
    """ Model that hold the company centers """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    center = models.CharField(max_length=30)

    def __str__(self):
        return self.center
