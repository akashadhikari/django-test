# Generated by Django 2.0 on 2018-01-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlist',
            name='client_pic',
            field=models.ImageField(default='.common/files/images/display.png', upload_to='.common/files/images'),
        ),
    ]