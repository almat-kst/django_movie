# Generated by Django 3.2 on 2021-05-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
    ]
