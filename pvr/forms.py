from pvr.models import Movies
from django import forms

class Movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields="__all__"