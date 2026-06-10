from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prospect
from propertytrack.models import Inspection
from .forms import ProspectForm

def prospect_phone_check(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        prospect = Prospect.objects.filter(phone=phone).first()
        
        if prospect:
            prospect.inspections.add(inspection)
            messages.success(request, f"{prospect.first_name} {prospect.last_name} already exists — added to inspection.")
            return redirect('propertytrack:in_inspection', rental_id=inspection.rental.id)
        else:
            return redirect('prospects:prospect_create', inspection_id=inspection_id, phone=phone)
    
    return render(request, 'prospects/prospect_phone_check.html', {'inspection': inspection})

def prospect_found(request, inspection_id, prospect_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    prospect = get_object_or_404(Prospect, id=prospect_id)
    
    if request.method == 'POST':
        prospect.inspections.add(inspection)
        messages.success(request, f"{prospect.first_name} signed in!")
        return redirect('propertytrack:in_inspection', rental_id=inspection.rental.id)
    
    return render(request, 'prospects/prospect_found.html', {'inspection': inspection, 'prospect': prospect})

def prospect_create(request, inspection_id, phone):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    
    if request.method == 'POST':
        prospect = Prospect.objects.create(
            phone=phone,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
        )
        prospect.inspections.add(inspection)
        messages.success(request, f"{prospect.first_name} added!")
        return redirect('propertytrack:in_inspection', rental_id=inspection.rental.id)
    
    return render(request, 'prospects/prospect_create.html', {'inspection': inspection, 'phone': phone})

def prospect_search(request):
    prospects = []
    if request.method == 'POST':
        search_value = request.POST.get('search_value')
        prospects = Prospect.objects.filter(phone__icontains=search_value) | Prospect.objects.filter(first_name__icontains=search_value)
    return render(request, 'prospects/prospect_search.html', {'prospects': prospects})

def prospect_update(request, prospect_id):
    prospect = get_object_or_404(Prospect, id=prospect_id)
    if request.method == 'POST':
        prospect.first_name = request.POST.get('first_name')
        prospect.last_name = request.POST.get('last_name')
        prospect.phone = request.POST.get('phone')
        prospect.notes = request.POST.get('notes')
        prospect.save()
        messages.success(request, "Prospect updated!")
        return redirect('prospects:prospect_detail', prospect_id=prospect.id)
    return render(request, 'prospects/prospect_update.html', {'prospect': prospect})

def prospect_detail(request, prospect_id):
    prospect = get_object_or_404(Prospect, id=prospect_id)
    inspections = prospect.inspections.all()
    return render(request, 'prospects/prospect_detail.html', {'prospect': prospect, 'inspections': inspections})