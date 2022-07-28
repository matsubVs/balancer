#!bin/bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn status_server.wsgi:application --bind 0.0.0.0:8005 --enable-stdio-inheritance