from django import forms
from .models import Rental

class RentalCreationForm(forms.ModelForm):
    class Meta:
        model = Rental 
        fields = [
            #'status'
            'address',
            #'address_number',
            #'address_suburb',
            #'address_postcode',
            #'bedrooms',
            #'bathrooms',
            #'car_spaces',
           # 'square_meters',
            #'owner_name',
            #'owner_email',
            #'owner_phone',
            #'tenant_name',
            #'tenant_phone',
            'rent_amount',
            #'bond_amount',
            #'created_at'
        ]