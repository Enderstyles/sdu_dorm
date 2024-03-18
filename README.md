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
localhost:8000/api/schema/docs          - SwaggerView
localhost:8000/api/profile/             - Profile API
localhost:8000/api/login/               - Login API
localhost:8000/api/about_pieces/        - About API
localhost:8000/api/forgot_password/     - Forgot api API
localhost:8000/api/logout/              - Logout API
localhost:8000/api/main_page/           - GET main page API
localhost:8000/api/edit_main_page/      - Edit main page API 
localhost:8000/api/news/                - News feed API
localhost:8000/api/news/<id>            - Get exact News post API
localhost:8000/news_categories/         - Get Category API
```
Default admin user
```
login:
    200000000
password:
    Admin12345 - same password for all users
```