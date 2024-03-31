from datetime import timedelta
from django.utils import timezone
from celery import shared_task
import sqlite3

from sdu_dorm.models import NewsPost, Enrollment


connect = sqlite3.connect("../sdu_dorm.db")
cursor = connect.cursor()


@shared_task(bind=True)
def test_task(self):
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def check_event(self):
    yesterday = timezone.now() - timedelta(days=1)
    print("yesterday: ", yesterday)
    news_posts_to_process = NewsPost.objects.filter(date_of_the_event=yesterday)
    ids_of_the_news_posts = news_posts_to_process.values_list('id', flat=True)
    for id_of_post in ids_of_the_news_posts:
        Enrollment.objects.filter(id=id_of_post).delete()
    return "Done"
