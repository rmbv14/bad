from django.forms import ModelForm #imports ModelForm
from .models import * #imports all our models
from django import forms    
class regform(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md bg-white focus:ring focus:ring-blue-300',
            'placeholder': 'Password'
        })
    )
    class Meta:
        model = Applicant_Information
        fields = ['first_name', 'last_name', 'password', 'number', 'email'] #uses all fields under the Profile model 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md'}),
            'number': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-300 rounded-md'}),
        }