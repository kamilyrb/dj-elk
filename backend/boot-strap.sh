echo "Running makemigrations"
./manage.py makemigrations
echo "Running migrate"
./manage.py migrate
echo "Loading data"
./manage.py runserver 0.0.0.0:8007

