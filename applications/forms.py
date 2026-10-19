from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

class NewApplicationForm(forms.Form):
    application_date = forms.DateTimeField(required=False) # Date application was submitted to company
    status = forms.CharField(max_length=50, default='1') # Interviewing, Applied, Prospective - Should be changed to a drop down or check box
    position = forms.CharField(max_length=250) # Company position of interest
    min_salary = forms.CharField(max_length=200, default="N/A") # Minimum Salary offered
    max_salary = forms.CharField(max_length=200, default="N/A") # Location of company
    contact_name = forms.CharField(max_length=250, default="N/A") # Name of contact person at company
    contact_phone = forms.CharField(max_length=250, default="") # Phone number of contact person at company
    company_location = forms.CharField(max_length=250, default="") # Location of company
    company_name = forms.CharField(max_length=250, default="") # Name of company
    resume = forms.FileField(allow_empty_file=True, max_length=250) # Resume file to be uploaded by user