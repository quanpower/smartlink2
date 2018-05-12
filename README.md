# smartlink2
smartlink2

## deploy

$ cp smartlink2/settings/local.py.example smartlink2/settings/local.py
$ echo "DJANGO_SETTINGS_MODULE=smartlink2.settings.local" > .env

pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser
./manage.py runserver