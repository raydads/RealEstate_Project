from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rental, Inspection
from .forms import RentalCreationForm
from django.utils import timezone

def home(request):
    return render(request, "propertytrack/home.html") 

def test_page(request):
    return render(request, "propertytrack/test.html")

def rental_create(request):
    if request.method == 'POST':
        form = RentalCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Property created!")
            return redirect('propertytrack:home')
    else:
        form = RentalCreationForm()
    return render(request, 'propertytrack/rentals/create.html', {'form': form})

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'propertytrack/rentals/list.html', {"rentals": rentals})

def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    inspections = Inspection.objects.filter(rental=rental).order_by('inspection_date')
    return render(request, 'propertytrack/rentals/detail.html', {
        'rental': rental,
        'inspections': inspections,
    })

def rental_update(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        rental.address = request.POST.get('address')
        rental.rent_amount = request.POST.get('rent_amount')
        rental.save()
        messages.success(request, "Property updated!")
        return redirect('propertytrack:rental_detail', pk=rental.id)
    return render(request, 'propertytrack/rentals/update.html', {'rental': rental})

def property_details(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    return render(request, 'propertytrack/rentals/property_details.html', {'rental': rental})

def inspection_list(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    inspections = Inspection.objects.filter(rental=rental)
    active = [i for i in inspections if i.get_status() in ['scheduled', 'in_progress']]
    return render(request, 'propertytrack/inspections/list.html', {'inspections': active, 'rental': rental})

def upcoming_inspections(request):
    now = timezone.now()
    inspections = Inspection.objects.filter(inspection_date__gte=now).order_by('inspection_date')
    return render(request, 'propertytrack/inspections/upcoming.html', {'inspections': inspections})

def inspection_create(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    if request.method == 'POST':
        inspection = Inspection.objects.create(
            rental=rental,
            inspection_date=request.POST.get('inspection_date'),
            notes=request.POST.get('notes')
        )
        messages.success(request, "Inspection created!")
        return redirect('propertytrack:inspection_detail', inspection_id=inspection.id)
    return render(request, 'propertytrack/inspections/create.html', {'rental': rental})

def inspection_detail(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    all_inspections = Inspection.objects.filter(rental=inspection.rental)
    return render(request, "propertytrack/inspections/detail.html", {
        "inspection": inspection,
        'all_inspections': all_inspections
    })

def inspection_edit(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    if request.method == 'POST':
        inspection.status = request.POST.get('status')
        inspection.save()
        messages.success(request, "Inspection updated!")
        return redirect('propertytrack:inspection_detail', inspection_id=inspection.id)
    return render(request, 'propertytrack/inspections/edit.html', {'inspection': inspection})

def in_inspection(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    inspections = Inspection.objects.filter(rental=rental)
    active = [i for i in inspections if i.get_status() in ['scheduled', 'in_progress']]
    return render(request, 'propertytrack/inspections/in_inspection.html', {'rental': rental, 'inspections': active})

def inspection_statistics(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    prospects = inspection.prospects.all()
    return render(request, 'propertytrack/inspections/statistics.html', {'inspection': inspection, 'prospects': prospects})

def completed_inspections(request):
    inspections = Inspection.objects.all()
    completed = [i for i in inspections if i.get_status() == 'completed']
    return render(request, 'propertytrack/inspections/completed.html', {'inspections': completed})

def completed_inspections_property(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    inspections = Inspection.objects.filter(rental=rental)
    completed = [i for i in inspections if i.get_status() == 'completed']
    return render(request, 'propertytrack/inspections/completed_property.html', {'rental': rental, 'inspections': completed})