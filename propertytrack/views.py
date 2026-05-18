from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rental, Inspection
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

def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    return render(request, 'propertytrack/rental_detail.html', {'rental': rental})

def rental_update(request, pk):
    rental = get_object_or_404(Rental, pk=pk)

    if request.method == 'POST':
        address = request.POST.get('address')
        rent_amount = request.POST.get('rent_amount')

        rental.address = address
        rental.rent_amount = rent_amount
        rental.save()

        messages.success(request, "property updated!")
        return redirect('propertytrack:rental_detail', pk=rental.id)
    
    return render(request, 'propertytrack/rental_update.html', {'rental': rental})


# @login_required
def inspection_detail(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)

    return render(request, "propertytrack/inspection_detail.html", {
        "inspection": inspection
    })

def inspection_create(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)

    if request.method == 'POST':
        inspection_date = request.POST.get('inspection_date')
        notes = request.POST.get('notes')

        inspection = Inspection.objects.create(
            rental=rental,
            inspection_date=inspection_date,
            notes=notes
        )

        messages.success(request, "Inspection Created!")

        return redirect(
            'propertytrack:inspection_detail',
            inspection_id=inspection.id
        )

    return render(request, 'propertytrack/inspection_create.html', {
        'rental': rental
    })
# @login_required
def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'propertytrack/rental_list.html', {"rentals": rentals})