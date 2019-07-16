from django import forms
from .models import *

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]

class ListForm_today(forms.ModelForm):
    class Meta:
        model = List_today
        fields = ["item", "completed"]
       
class ListForm_week(forms.ModelForm):
    class Meta:
        model = List_thisweek
        fields = ["item", "completed"]

class ListForm_month(forms.ModelForm):
    class Meta:
        model = List_thismonth
        fields = ["item", "completed"]

class ListForm_spare(forms.ModelForm):
    class Meta:
        model = List_spare_time
        fields = ["item", "completed"]

