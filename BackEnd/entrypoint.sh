#!/bin/bash
# window에서 수정시 아래 링크 참고
# https://www.jetbrains.com/help/pycharm/configuring-line-endings-and-line-separators.html

echo "Apply database migrations"
python manage.py migrate
python manage.py migrate --database=test

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000