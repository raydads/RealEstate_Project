from django.db import models
from propertytrack.models import Inspection
# Create your models here.

class Prospect(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    inspections = models.ManyToManyField(Inspection, related_name='prospects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"