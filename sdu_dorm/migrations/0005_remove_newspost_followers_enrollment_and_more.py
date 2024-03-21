# Generated by Django 4.2.10 on 2024-03-21 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdu_dorm', '0004_newspost_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='followers',
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdu_dorm.newspost')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='follows',
            field=models.ManyToManyField(through='sdu_dorm.Enrollment', to='sdu_dorm.newspost'),
        ),
    ]
