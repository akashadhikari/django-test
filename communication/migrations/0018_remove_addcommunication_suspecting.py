# Generated by Django 2.0 on 2018-01-23 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0017_auto_20180123_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcommunication',
            name='suspecting',
        ),
    ]
