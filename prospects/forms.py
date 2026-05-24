from django import forms
from .models import Prospect

class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect 
        fields = [
            "first_name",
            "last_name",
            "phone"
        ]