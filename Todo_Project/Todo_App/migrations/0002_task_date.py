# Generated by Django 4.1.7 on 2023-04-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Date',
            field=models.DateField(default='1989-02-21'),
            preserve_default=False,
        ),
    ]