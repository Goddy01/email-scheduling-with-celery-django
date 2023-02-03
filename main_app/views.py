import json
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('Done!')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent to all users.")

def schedule_mail(request):
    # You can get details of the task from the admin as inputs then use it to create unique instances of CrontabSchedule and PeriodicTask
    schedule, created = CrontabSchedule.objects.get_or_create(hour=15, minute=46)
    task = PeriodicTask.objects.create(task='send_mail_app.tasks.send_mail_func', crontab=schedule, name='schedule_mail_task' + '5') # args=json.dumps([[3, 9]]))
    return HttpResponse("Mail Scheduled.")