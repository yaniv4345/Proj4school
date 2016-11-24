from django import forms
from django.db import models
from .models import person
class insertForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['name','id_number','age','address']
        name = forms.CharField(label = 'Name', help_text='Enter the student name')
        id_number = forms.IntegerField(label='ID Number', help_text='Enter the student ID number')
        age = forms.IntegerField(label='Age', help_text="Enter the student age",  widget=forms.TextInput)
        address = forms.CharField(label='Address', help_text='Enter the student address')
