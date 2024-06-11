from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    img_preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение(превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    pur_price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания(записи в БД)')
    updated_at = models.DateTimeField(default=datetime.now, verbose_name='Дата последнего изменения(записи в БД)')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contacts(models.Model):
    country = models.CharField(max_length=50, verbose_name='страна')
    inn = models.CharField(max_length=15, verbose_name='инн')
    address = models.CharField(max_length=100, verbose_name='адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return f'{self.country}'


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_images/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'