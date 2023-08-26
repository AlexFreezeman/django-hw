from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=25, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

