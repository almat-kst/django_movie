# Generated by Django 3.2 on 2021-05-03 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_acror_movie_actor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='acror',
        ),
    ]