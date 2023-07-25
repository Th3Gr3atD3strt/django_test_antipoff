from django.forms import Form
from django import forms


class QueryForm(Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    unicue_id = forms.CharField()