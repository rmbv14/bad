from django.shortcuts import render
from django.http import HttpResponse

def Profile(request):
    return render(request, 'demo_app/base.html')

def Reg(request):
    return render(request, 'demo_app/reg.html')
# Create your views here.
