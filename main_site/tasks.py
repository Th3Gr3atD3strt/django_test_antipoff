import time

import requests
from celery import shared_task

'''celery -A django_test_antipoff worker --loglevel=info'''

@shared_task
def delayed_request(data):
    try:
        ans = requests.post(url='https://echo.zuplo.io/', json=data)
        print('WE WE GOT AN ANSWER!!!!!')
        if ans:
            return True
        else:
            return False
    except:
        return False