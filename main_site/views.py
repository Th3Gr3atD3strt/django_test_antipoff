import requests
from django.http import HttpResponse
from django.shortcuts import render

from main_site.forms import QueryForm


def main_view(request):
    form = QueryForm()
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                ans = requests.get(f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_objects/{data["unicue_id"]}')
                print(ans)
            except:
                return HttpResponse('сервер не ответил')
    return render(request, 'main_site/main_site.html', {'form':form} )

