Write this commands to start project:

To install all necessary dependencies 
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
localhost:8000/api/schema/docs   - SwaggerView
localhost:8000/api/profile/      - Profile API
localhost:8000/api/login/         - Login API
localhost:8000/api/about_pieces/ - About API
localhost:8000/api/forgot_password/
localhost:8000/api/logout/
localhost:8000/api/main_page/
localhost:8000/api/edit_main_page/
```
Default admin user
```
login:
    200000000
password:
    Admin12345 - same password for all users
```