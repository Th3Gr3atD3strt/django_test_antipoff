import json
import threading
import requests
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_site.forms import QueryForm, UserForm
from main_site.functions import send_http_query
from main_site.models import QueryModel


def main_view(request):
    form = QueryForm()
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            thread = threading.Thread(target=send_http_query, args=(request, data))
            thread.start()
            return redirect('result')
    return render(request, 'main_site/main_site.html', {'form':form} )

def result_view(request):
    answers = QueryModel.objects.filter(user=User.objects.get(pk=request.user.pk))

    return render(request, 'main_site/result.html', {'answers': answers})

class Loginator(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_site/login.html'

    def get_success_url(self):
        return reverse_lazy('query')

class Registrator(CreateView):
    form_class = UserCreationForm
    template_name = 'main_site/register.html'

    def get_success_url(self):
        return reverse_lazy('query')

def logout_view(request):
    logout(request)
    return redirect('auth')
