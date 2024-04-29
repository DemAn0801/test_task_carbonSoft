#!/bin/sh
set -e

export DJANGO_SETTINGS_MODULE=$DSM
python src/manage.py migrate

python src/manage.py runserver 0.0.0.0:8000
exec "$@"
