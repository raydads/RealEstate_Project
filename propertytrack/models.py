import uuid
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Rental(models.Model):
    #all the fields
    #status = models.Charfield(max_length=20, default='vacant')

    #address block 
    address = models.CharField(max_length=255)
    #address_number = models.CharField(max_length=5)
    #address_suburb = models.CharField(max_length=255)
    #address_postcode = models.CharField(max_length=4)

    # property detail block Add max length validator 
    #bedrooms = models.IntegerField()
    #bathrooms = models.IntegerField()
   # car_spaces = models.IntegerField()
    #square_meters = models.IntegerField() # if none of these are provided, we can set them to 0 or null

    # owner detail block 
    #owner_name = models.CharField(max_length=255)
    #owner_email = models.EmailField()
    #owner_phone = models.CharField(max_length=20)

    # tenant detail block
    #tenant_name = models.CharField(max_length=255, blank=True, null=True)
    #tenant_phone = models.CharField(max_length=20, blank=True, null=True)

    # financial detail block
    rent_amount = models.DecimalField(max_digits=8, decimal_places=2)
    #bond_amount = models.DecimalField(max_digits=10, decimal_places=2)

    #timestamps 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Inspection(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"Inspection - {self.rental.address}"

