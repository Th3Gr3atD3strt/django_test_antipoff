#docker build -t django_proj .
#docker run -p 8000:8000 django_proj
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /antipoff_proj
ADD . /antipoff_proj/
WORKDIR /antipoff_proj

RUN pip install -r requirements.txt
RUN python manage.py migrate

#RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('vitya1', 'vity.elsakov@gmail.com', 'vitya1')" | python manage.py shell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]