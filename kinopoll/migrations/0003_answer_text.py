# Generated by Django 3.1.5 on 2021-01-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoll', '0002_auto_20210122_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
