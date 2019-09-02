from django import forms

class ApplForm(forms.Form):
    First_name = forms.CharField(label='First name', max_length=100)
    Last_name = forms.CharField(label='First name', max_length=100)