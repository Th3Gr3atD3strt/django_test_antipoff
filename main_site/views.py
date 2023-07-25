import json
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main_site.forms import QueryForm
from main_site.tasks import delayed_request


def main_view(request):
    form = QueryForm()
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            res = delayed_request.delay(data)
            return redirect('query')
    return render(request, 'main_site/main_site.html', {'form':form} )

