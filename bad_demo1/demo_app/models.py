from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# import random
#pip install django-phonenumber-field phonenumbers

class Applicant_Information(models.Model): #the main model for applicant info
    # student_id = models.IntegerField(primary_key=True, unique=True, editable=False, max_length=6)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(region="PH")
    email = models.CharField(max_length=50)
    
    # def save(self, *args, **kwargs):
    #     if not self.student_id:  # Only generate an ID if it is not already set
    #         while True:
    #             new_id = random.randint(100000, 999999)  # Generate a 6-digit number
    #             if not Applicant_Information.objects.filter(student_id=new_id).exists():
    #                 self.student_id = new_id
    #                 break
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
