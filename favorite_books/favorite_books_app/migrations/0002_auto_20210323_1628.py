# Generated by Django 2.2 on 2021-03-23 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='description',
        ),
    ]
