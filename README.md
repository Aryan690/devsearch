# :computer: DevSearch - Connect With Developers From Around The World!

### Technologies Stack
- Django
- PostgreSQL
- HTML / CSS

### Developed By
- [aryansetia](https://github.com/aryansetia)
- Templates for frontend were taken from [divanov11/Django-2021](https://github.com/divanov11/Django-2021)

### Website Features
- Browse and search for developers
- Browse and search for projects
- Sign up and log in into account
- Edit / Delete account information
- Create / Edit / Delete your projects
- Comment other's projects
- Send messages to developers / Read your inbox messages
- Reset password to your account via email

### Preview
# Home Page

<img src="./images/Devsearch Home.jpg">  

# Projects Page
<img src="./images/DevSearch Projects.jpg">  

# Profile Page
<img src="./images/Devsearch Profile.jpg">  

# User Inbox
<img src="./images/Devsearch Inbox.jpg">  


### Run it yourself
```sh
git clone https://github.com/h4cktivist/devSearch.git
cd devSearch
pip install - r requirements.txt
```

Create a `.env` file in the root of your Django-project, add a key like;
`SECRET_KEY=SomeSecretKeyHere`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'devsearch',
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}
```
Then run the migrations:
```sh
python manage.py migrate
```

Also change this up to your email for reset password confirmation feature
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
```

Then you can run it
```sh
python manage.py runserver
```
