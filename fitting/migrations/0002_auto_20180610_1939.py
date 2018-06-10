# Generated by Django 2.0.6 on 2018-06-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hull',
            name='hull_class',
            field=models.TextField(choices=[('shuttle', 'SHUTTLE'), ('frigate', 'FRIGATE'), ('cruiser', 'CRUISER')]),
        ),
        migrations.AlterField(
            model_name='hull',
            name='name',
            field=models.TextField(max_length=40, verbose_name='Hull name'),
        ),
    ]