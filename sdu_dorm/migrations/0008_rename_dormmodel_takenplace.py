# Generated by Django 4.2.10 on 2024-03-31 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0007_dormmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DormModel',
            new_name='TakenPlace',
        ),
    ]