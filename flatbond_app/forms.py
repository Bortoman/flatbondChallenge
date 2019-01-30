from django import forms

class FlatbondForm(forms.Form):
    rent_week = forms.IntegerField(label="Rent per Week", min_value=25, max_value=2000)
    rent_month = forms.IntegerField(label="Rent per Month", min_value=2000, max_value=8660)
    
