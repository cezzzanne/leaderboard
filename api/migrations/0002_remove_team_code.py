# Generated by Django 2.0.5 on 2020-01-11 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='code',
        ),
    ]
