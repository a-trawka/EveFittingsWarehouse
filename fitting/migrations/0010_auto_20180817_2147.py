# Generated by Django 2.0.6 on 2018-08-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitting', '0009_auto_20180817_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.TextField(unique=True, verbose_name='Module name'),
        ),
    ]
