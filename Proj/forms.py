from django import forms
from django.db import models
from .models import person
from .id_check import id_checker
class insertForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = person
        fields = ['name','id_number','age','address']
        name = forms.CharField(label = 'Name', help_text='Enter the student name')
        id_number = forms.IntegerField(label='ID Number', help_text='Enter the student ID number')
        age = forms.IntegerField(label='Age', help_text="Enter the student age",  widget=forms.TextInput)
        address = forms.CharField(label='Address', help_text='Enter the student address')

    def clean(self):
        super(insertForm,self).clean()
        try:
            number = self.cleaned_data.get('id_number')
            if id_checker(str(number)):
                raise forms.ValidationError("{} is not a valid id number.".format(number),code = 'realid')
        except person.DoesNotExist:
            return self.cleaned_data
