# Generated by Django 4.0.4 on 2022-05-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('order', models.PositiveIntegerField(max_length=7)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price, USD')),
                ('delivery_time', models.DateField()),
                ('price_rur', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price, RUR')),
            ],
        ),
    ]
