# Generated by Django 3.2.7 on 2021-09-25 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
