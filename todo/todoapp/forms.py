# from dataclasses import fields
# from pyexpat import model
from django import forms 
from . models import Todo


class Todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'