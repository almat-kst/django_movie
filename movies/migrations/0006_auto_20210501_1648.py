# Generated by Django 3.2 on 2021-05-01 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Звезда рейтинга актера', 'verbose_name_plural': 'Звезды рейтинга актера'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'verbose_name': 'Звезда рейтинга фильма', 'verbose_name_plural': 'Звезды рейтинга фильма'},
        ),
    ]