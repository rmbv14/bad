from django.contrib import admin
from .models import * #imports all the models from models.py


admin.site.register(Applicant_Information) #registers the model to the database for admin

# Register your models here.
