from django import forms


class CodeGetter(forms.Form):
    City = forms.CharField(max_length=200)
    

class CityGetter(forms.Form):
    Code = forms.CharField(max_length=4)