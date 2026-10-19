from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

class NewApplicationForm(forms.Form):
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