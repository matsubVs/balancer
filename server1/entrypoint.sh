#!bin/bash
gunicorn server1.wsgi:application -w 4 --bind 0.0.0.0:8001 --enable-stdio-inheritance