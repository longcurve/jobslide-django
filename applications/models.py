from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # JobSlide user who added application
    posted_date = models.DateTimeField(default=timezone.now) # Date job application was saved by user
    application_date = models.DateTimeField(blank=True, null=True) # Date application was submitted to company
    status = models.CharField(max_length=50) # True/False - Should be changed to a drop down or check box
    position = models.CharField(max_length=250) # Company position of interest
    min_salary = models.CharField(max_length=200, default="") # Minimum Salary offered
    max_salary = models.CharField(max_length=200, default="") # Maxmium Salary offered
    company = models.CharField(max_length=250) # Company offering position
    location = models.CharField(max_length=250) # Location of company
    contact_name = models.CharField(max_length=250, default="") # Name of contact person at company
    contact_phone = models.CharField(max_length=250, default="") # Phone number of contact person at company
    



def publish(self):
    self.posted_date = timezone.now()
    self.save()

def __str__(self):
    return self.position + ' - ' + self.company