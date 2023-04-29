from django import forms
from pa.models import Acc

class Myform(forms.ModelForm):
    class Meta:
        model=Acc
        fields='__all__'
