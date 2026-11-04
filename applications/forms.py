from django import forms
from django.core.validators import MinLengthValidator
from django.db import models
from .models import Post

APPLICATION_STATUS_CHOICES = [
    ('1', 'Prospective'),
    ('2', 'Applied'),
    ('3', 'Interviewing'),
    
]

#class NewApplicationForm(forms.Form):
 #   application_date = forms.DateTimeField(required=False) # Date application was submitted to company
  #  status = forms.CharField(max_length=1) # Interviewing, Applied, Prospective - Should be changed to a drop down or check box
   # position = forms.CharField(max_length=250) # Company position of interest
   # min_salary = forms.CharField(max_length=200) # Minimum Salary offered
   # max_salary = forms.CharField(max_length=200) # Location of company
   # contact_name = forms.CharField(max_length=250) # Name of contact person at company
   # contact_phone = forms.CharField(max_length=250) # Phone number of contact person at company
   # company_location = forms.CharField(max_length=250) # Location of company
   # company_name = forms.CharField(max_length=250) # Name of company
  #  resume = forms.CharField(max_length=250) # Name of Resume used to apply

class NewApplication(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['application_date', 'status', 'position', 'min_salary', 'max_salary', 'contact_name', 'contact_phone', 'company_location', 'company_name', 'resume']