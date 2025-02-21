from django.forms import ModelForm #imports ModelForm
from .models import * #imports all our models

class regform(ModelForm):
    class Meta:
        model = Applicant_Information
        fields = '__all__' #uses all fields under the Profile model 
