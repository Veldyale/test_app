# Generated by Django 4.0.4 on 2022-05-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0005_rename_order_sheet_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='delivery_time',
            field=models.DateField(),
        ),
    ]
