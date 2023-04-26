#!/bin/bash

cd /app/api

python manage.py migrate

exec "$@"