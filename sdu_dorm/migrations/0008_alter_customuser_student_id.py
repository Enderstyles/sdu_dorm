# Generated by Django 4.2.10 on 2024-02-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0007_alter_customuser_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.CharField(max_length=9, unique=True, verbose_name='student_id'),
        ),
    ]
