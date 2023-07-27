from django.contrib.auth.models import User
from django.forms import Form
from django import forms


class QueryForm(Form):
    latitude = forms.FloatField(label='Широта')
    longitude = forms.FloatField(label='Долгота')
    number = forms.CharField(label='Кадастровый номер')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']