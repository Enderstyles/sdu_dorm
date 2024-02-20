Write this commands to start project:

To install all necessaries dependencies 
```
pip install -r requirements.txt
```
To create tables 
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
To create admin profile write
```
python manage.py createsuperuser
```
To start project 
```
python manage.py runserver
```
APIs
```
localhost:8000/api/schema/docs  - SwaggerView
localhost:8000/api/students     - Students API
localhost:8000/api/about_pieces - About API
```
