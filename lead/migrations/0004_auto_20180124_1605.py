# Generated by Django 2.0 on 2018-01-24 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('lead', '0003_auto_20180117_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadprocess',
            old_name='post_choice',
            new_name='stages',
        ),
        migrations.RemoveField(
            model_name='leadprocess',
            name='post_type',
        ),
        migrations.AddField(
            model_name='leadprocess',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client_lead', to='client.AddClient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadprocess',
            name='service_type',
            field=models.CharField(choices=[('Top Jobs', 'Top Jobs'), ('Hot Jobs', 'Hot Jobs'), ('F. Post', 'F. Post'), ('G. Post', 'G. Post')], max_length=15),
        ),
    ]
