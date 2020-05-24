Steps for setting up the environment

create virtual environment

virtualenv vrtl_nv

activate virtual environment

source vrtl_nv/bin/activate

install requirements

pip install -r requirements.txt

run following commands

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
