# Generated by Django 4.2.10 on 2024-03-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0002_newscategories_newspost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='what_to_expect',
            field=models.TextField(blank=True),
        ),
    ]
