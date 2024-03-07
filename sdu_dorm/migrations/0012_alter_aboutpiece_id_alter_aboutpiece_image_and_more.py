# Generated by Django 4.2.10 on 2024-03-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0011_alter_customuser_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpiece',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='aboutpiece',
            name='image',
            field=models.FileField(upload_to='../media/about'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='media/profile_pics/default.jpg', upload_to='../media/profile_pics'),
        ),
    ]