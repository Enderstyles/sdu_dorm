# Generated by Django 4.2.10 on 2024-04-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0006_customuser_citizenship'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenshipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('value', models.CharField(max_length=1)),
            ],
        ),
    ]