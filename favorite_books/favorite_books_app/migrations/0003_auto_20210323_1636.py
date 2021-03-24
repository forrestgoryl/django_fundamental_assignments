# Generated by Django 2.2 on 2021-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0002_auto_20210323_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_who_like',
        ),
        migrations.AddField(
            model_name='book',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='favorite_books_app.User'),
        ),
    ]