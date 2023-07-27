#docker build -t django_proj .
#docker run -p 8000:8000 django_proj
# Используем базовый образ Python 3.8
FROM python:3.8-slim-buster

# Устанавливаем переменную окружения для Python
ENV PYTHONUNBUFFERED 1

# Создаем директорию для нашего проекта
RUN mkdir /code

# Копируем все файлы из текущей директории в директорию /code
ADD . /code/

# Устанавливаем рабочую директорию
WORKDIR /code

# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r requirements.txt


RUN python manage.py migrate


#RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('vitya', 'vity.elsakov@gmail.com', 'vitya')" | python manage.py shell

# Открываем порт 8000 для доступа к Django приложению
EXPOSE 8000

# Запускаем Django сервер
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]