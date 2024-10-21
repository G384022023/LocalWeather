from django import forms
from django.forms import ModelForm
from .models import currentConditions

class LocationForm(forms.Form):
    zip = forms.CharField(label = "Zip Code", max_length = 5)
    state = forms.CharField(label = "State", max_length = 2)
    city = forms.CharField(label = "City", max_length = 100)

class ConditionsForm(ModelForm):
    class Meta:
        model = currentConditions 
        fields = '__all__'

