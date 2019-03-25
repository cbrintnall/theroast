from django import forms

from roast.models import Roast

class RoastForm(forms.ModelForm):
    class Meta:
        model = Roast
        fields = ('name', 'color')