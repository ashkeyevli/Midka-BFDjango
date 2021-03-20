# Generated by Django 3.1.6 on 2021-03-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'SuperAdmin'), (2, 'Guest')], default=2),
        ),
    ]
