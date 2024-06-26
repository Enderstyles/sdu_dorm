# Generated by Django 4.2.10 on 2024-04-29 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0011_alter_uploaddocumentsmodel_address_certificate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='takenplaces',
            name='payment',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='sdu_dorm.paymentmodel'),
        ),
    ]
