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
        'NAME': 'dvgv8sgqkakrd',
        'HOST': 'ec2-79-125-4-96.eu-west-1.compute.amazonaws.com',
        'USER': 'uqndlrerapeuiz',
        'PASSWORD': '0eea8c014a9519333d9a1b40ce93cbfa9e8291583f8787381bc66bbb0b3f6c28',
    }
}
