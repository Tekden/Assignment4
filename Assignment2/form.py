__author__ = 'talhatekden'
from django import forms


class teachersform(forms.Form):
    first_name= forms.CharField(max_length=20)
    last_name= forms.CharField(max_length=20)
    office_details=forms.CharField(max_length=40)
    phone_number=forms.CharField(max_length=20)
    email = forms.EmailField()

class studentsform(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class coursesform(forms.Form):
    name = forms.CharField(max_length=40)
    code = forms.CharField(max_length=15)
    classroom = forms.CharField(max_length=15)
    times = forms.DateTimeField()
    teacher = forms.CharField()
    students =forms.CharField()