# Generated by Django 2.0 on 2018-01-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0024_addcommunication_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleslead',
            name='client',
        ),
        migrations.RemoveField(
            model_name='saleslead',
            name='communication',
        ),
        migrations.RemoveField(
            model_name='saleslead',
            name='user',
        ),
        migrations.AddField(
            model_name='addcommunication',
            name='medium_status',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='SalesLead',
        ),
    ]
