# Generated by Django 4.1.5 on 2023-01-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='Stock',
        ),
    ]
