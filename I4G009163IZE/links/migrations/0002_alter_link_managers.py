# Generated by Django 4.0.6 on 2022-07-17 19:29

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='link',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]