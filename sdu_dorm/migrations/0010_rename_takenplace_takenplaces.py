# Generated by Django 4.2.10 on 2024-04-23 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0009_alter_customuser_citizenship_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TakenPlace',
            new_name='TakenPlaces',
        ),
    ]
