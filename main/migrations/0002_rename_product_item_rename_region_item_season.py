# Generated by Django 4.2.5 on 2023-09-08 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='region',
            new_name='season',
        ),
    ]
