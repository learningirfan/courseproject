from django import forms
from django.forms import ModelForm, DateField
from .models import Exps


class ExpsForm(forms.ModelForm):
    class Meta:
        model = Exps
        fields =["date", "amt", "cat", "ven", "cap", "pmeth"]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),

        }
