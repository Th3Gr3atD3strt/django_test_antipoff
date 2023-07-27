import json
import requests
from django.contrib.auth.models import User
from main_site.models import QueryModel

def send_http_query(request, data):
    data1 = json.loads(data)
    latitude, longitude, number = data1['latitude'], data1['longitude'], data1['number']
    try:
        a = requests.post(data=data, url='https://echo.zuplo.io', timeout=60)

        if a.status_code == 200:
            QueryModel.objects.create(lattidute=latitude,
                                      longitude=longitude,
                                      number=number,
                                      result=True,
                                      user=User.objects.get(pk=request.user.id)
                                      )
        else:
            QueryModel.objects.create(lattidute=latitude,
                                      longitude=longitude,
                                      number=number,
                                      result=False,
                                      user=User.objects.get(pk=request.user.id)
                                      )
    except:
        QueryModel.objects.create(lattidute=latitude,
                                  longitude=longitude,
                                  number=number,
                                  result=False,
                                  user=User.objects.get(pk=request.user.id)
                                  )