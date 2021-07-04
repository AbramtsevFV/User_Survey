set -e
pipenv run python manage.py migrate --noinput
pipenv run python manage.py loaddata .fi
pipenv run python manage.py runserver 0.0.0.0:8000