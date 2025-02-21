from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def Profile(request):
    return render(request, 'demo_app/base.html')

def Reg(request):
    form = regform()
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form=regform
    return render(request, 'demo_app/reg.html', {'form':form})
# Create your views here.
