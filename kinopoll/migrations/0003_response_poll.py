# Generated by Django 3.1.5 on 2021-01-17 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoll', '0002_auto_20210117_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='kinopoll.poll'),
            preserve_default=False,
        ),
    ]
