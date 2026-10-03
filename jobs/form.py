from django import forms
from .models import Job


class Jobform(form.ModelForm):
    class Meta:
        model=Job
        fields = ['title','company_name','description','location','salary']