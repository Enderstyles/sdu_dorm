# Generated by Django 4.2.10 on 2024-05-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0015_paymentmodel_id_alter_paymentmodel_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
            ],
        ),
    ]
