# Generated by Django 4.0.8 on 2023-01-16 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-created_at',)},
        ),
    ]
