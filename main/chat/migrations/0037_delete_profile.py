# Generated by Django 4.1.4 on 2023-03-01 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0036_alter_post_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
