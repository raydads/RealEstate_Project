from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='agents/login') 
def home(request):
    return render(request, "propertytrack/home.html") 


def test_page(request):
    return render(request, "propertytrack/test.html")