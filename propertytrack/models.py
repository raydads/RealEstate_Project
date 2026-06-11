import uuid
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Rental(models.Model):
    address = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_archived = models.BooleanField(default=False)
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
    
    def get_status(self):
        now = timezone.now()
        if now < self.inspection_date:
            return 'scheduled'
        elif now > self.inspection_date + timezone.timedelta(hours=2):
            return 'completed'
        else:
            return 'in_progress'
