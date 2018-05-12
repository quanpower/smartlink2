# smartlink2
smartlink2


$ cp bakerydemo/settings/local.py.example smartlink2/settings/local.py
$ echo "DJANGO_SETTINGS_MODULE=smartlink2.settings.local" > .env


./manage.py migrate
./manage.py load_initial_data
./manage.py runserver