# Generated by Django 5.0 on 2023-12-29 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0002_alter_fruit_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='description',
            new_name='description2',
        ),
    ]
