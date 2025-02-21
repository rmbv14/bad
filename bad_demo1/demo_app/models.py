from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#pip install django-phonenumber-field phonenumbers

class Applicant_Information(models.Model): #the main model for applicant info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    number = PhoneNumberField(region="PH")
    email = models.CharField(max_length=50)
# Create your models here.
