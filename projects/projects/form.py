from django import forms

class Project_form(forms.Form):
    name = forms.CharField(max_length=1024)
    comment = forms.CharField(max_length=4096)
