# Generated by Django 4.2.10 on 2024-02-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0004_rename_username_customuser_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='student_id'),
        ),
    ]