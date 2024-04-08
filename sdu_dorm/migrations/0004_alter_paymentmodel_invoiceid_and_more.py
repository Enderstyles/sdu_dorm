# Generated by Django 4.2.10 on 2024-04-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0003_paymentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='invoiceID',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='token',
            field=models.TextField(unique=True),
        ),
    ]
