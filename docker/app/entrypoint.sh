#! /bin/bash

cd ./src || exit

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec daphne -b 0.0.0.0 -p 8000 fast-ml-mvp.asgi:application