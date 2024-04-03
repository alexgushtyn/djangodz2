# Generated by Django 5.0.3 on 2024-04-03 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('inn', models.CharField(max_length=15, verbose_name='странао')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания(записи в БД)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pur_price',
            field=models.FloatField(verbose_name='Цена за покупку'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата последнего изменения(записи в БД)'),
        ),
    ]