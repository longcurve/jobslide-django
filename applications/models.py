from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Userho added an application entry
    posted_date = models.DateTimeField(default=timezone.now) # Date job application was saved by user
    application_date = models.DateTimeField(blank=True, null=True) # Date application was submitted to company
    status = models.CharField(max_length=50, default='1') # Interviewing, Applied, Prospective - Should be changed to a drop down or check box
    position = models.CharField(max_length=250) # Company position of interest
    min_salary = models.CharField(max_length=200, default="") # Minimum Salary offered
    max_salary = models.CharField(max_length=200, default="N/A") # Location of company
    contact_name = models.CharField(max_length=250, default="") # Name of contact person at company
    contact_phone = models.CharField(max_length=250, default="") # Phone number of contact person at company
    company_location = models.CharField(max_length=250, default="") # Location of company
    company_name = models.CharField(max_length=250, default="") # Name of company
    resume = models.FileField(upload_to='resumes/', blank=True, null=True) # Resume file uploaded by user

def publish(self):
    self.posted_date = timezone.now()
    self.save()

def __str__(self):
    return self.position + ' - ' + self.company