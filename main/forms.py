from django import forms
from .models import Requirements

class Requirementsform(forms.ModelForm):

    class Meta:
        model = Requirements
        fields = ['equipments','quantity','description','reason','required_by','additional',]