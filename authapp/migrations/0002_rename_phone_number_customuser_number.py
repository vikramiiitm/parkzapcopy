# Generated by Django 4.0 on 2021-12-15 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='number',
        ),
    ]
