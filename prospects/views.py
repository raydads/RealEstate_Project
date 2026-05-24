from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prospect
from .forms import ProspectForm
# Create your views here.

def prospect_create(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    prospect = None
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Search for existing prospect by phone
        prospect = Prospect.objects.filter(phone=phone).first()
        
        if not prospect:
            # Create new prospect if not found
            prospect = Prospect.objects.create(
                phone=phone,
                first_name=first_name,
                last_name=last_name
            )
        
        prospect.inspections.add(inspection)
        messages.success(request, f"Prospect {prospect.first_name} added!")
        
        return redirect('propertytrack:inspection_detail', inspection_id=inspection.id)
    
    return render(request, 'prospects/prospect_create.html', {'inspection': inspection, 'prospect': prospect})

def prospect_search(request):
    prospects = []
    if request.method == 'POST':
        search_value = request.POST.get('search_value')
        prospects = Prospect.objects.filter(phone__icontains=search_value) | Prospect.objects.filter(first_name__icontains=search_value)
    
    return render(request, 'prospects/prospect_search.html', {'prospects': prospects})
