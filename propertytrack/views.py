from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rental
from .forms import RentalCreationForm

# @login_required(login_url='agents/login') 
def home(request):
    return render(request, "propertytrack/home.html") 


def test_page(request):
    return render(request, "propertytrack/test.html")

# @login_required(login_url='agents:login') only for now while testing 
def rental_create(request):
    if request.method == 'POST':
        form = RentalCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Property created!")
            return redirect('propertytrack:home')
    else:
        form = RentalCreationForm()
    
    return render(request, 'propertytrack/rental_create.html', {'form': form})