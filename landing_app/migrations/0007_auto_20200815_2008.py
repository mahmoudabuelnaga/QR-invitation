# Generated by Django 2.2.15 on 2020-08-15 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0006_ourclients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurClients',
            new_name='OurClient',
        ),
    ]