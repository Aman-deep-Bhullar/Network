from django import forms
from .models import Item

class ListForm(forms.ModelForm):
    class Meta:
        model =Item
        fields =["post", "timestamp"]


