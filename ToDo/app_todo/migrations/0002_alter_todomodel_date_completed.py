# Generated by Django 3.2 on 2022-02-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
