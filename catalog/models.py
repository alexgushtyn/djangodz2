from django.db import models

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
    pur_price = models.DecimalField(max_digits=1000, decimal_places=0, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания(записи в БД)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения(записи в БД')


    def __str__(self):
        return f'{self.name} ({self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'