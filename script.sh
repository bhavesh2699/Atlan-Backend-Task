#!/bin/sh

celery -A Collect worker -l info &
gunicorn --bind 0.0.0.0:8000 Collect.wsgi:application