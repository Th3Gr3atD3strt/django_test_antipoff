FROM python:3.8-slim-buster

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        postgresql-client redis-server

# Копируем файлы проекта в контейнер
COPY . /app
WORKDIR /app

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Определяем переменные окружения
ENV DJANGO_SETTINGS_MODULE=myproject.settings.production
ENV PYTHONUNBUFFERED=1

# Запускаем Celery в фоновом режиме
CMD celery -A myproject worker -l info & \
    python manage.py runserver 0.0.0.0:8000