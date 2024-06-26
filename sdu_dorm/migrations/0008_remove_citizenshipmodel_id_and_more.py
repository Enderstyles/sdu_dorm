# Generated by Django 4.2.10 on 2024-04-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0007_citizenshipmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizenshipmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='citizenshipmodel',
            name='value',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='citizenship',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='sdu_dorm.citizenshipmodel'),
        ),
    ]
