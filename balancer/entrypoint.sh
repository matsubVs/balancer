#!bin/bash
gunicorn balancer.wsgi:application --bind 0.0.0.0:8004 --enable-stdio-inheritance