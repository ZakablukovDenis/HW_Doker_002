# Generated by Django 4.1.7 on 2023-05-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='director-mail@gmail.com', max_length=254),
        ),
    ]
