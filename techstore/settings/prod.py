from .base import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ADMINS = (
    ('Mohamed Youssef', 'mu7med.youssef@gmail.com'),
)
ALLOWED_HOSTS = ['techstor.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'techstore',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '123456',
    }
}
