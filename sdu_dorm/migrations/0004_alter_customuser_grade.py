# Generated by Django 4.2.10 on 2024-03-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0003_alter_newspost_what_to_expect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.FloatField(blank=True, default=1),
        ),
    ]