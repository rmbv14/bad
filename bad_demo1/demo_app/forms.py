from django.forms import ModelForm
from .models import *

class regform(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        