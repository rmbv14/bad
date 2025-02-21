from django.shortcuts import render, redirect #allows us to render and redirect html pages
from django.http import HttpResponse #idt we need this anymore
from .forms import * #imports all forms from forms.py 

def Profile(request):
    return render(request, 'demo_app/base.html') #renders base.html 

def Register(request):
    form = regform() #idk how any of this below works it just does
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form=regform
    return render(request, 'demo_app/register.html', {'form':form})
# Create your views here.
