# Generated by Django 4.0.4 on 2022-05-20 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='number',
        ),
    ]
