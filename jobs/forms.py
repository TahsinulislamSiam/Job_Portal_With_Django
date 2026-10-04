from django import forms
from .models import Job

class Jobform(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            'title',
            'company_name',
            'location',
            'salary',
            'description',
        ]
