from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    desc = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = ResizedImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
