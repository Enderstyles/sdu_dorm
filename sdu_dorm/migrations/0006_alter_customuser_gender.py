# Generated by Django 4.2.10 on 2024-03-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0005_remove_newspost_followers_enrollment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(default=True),
        ),
    ]