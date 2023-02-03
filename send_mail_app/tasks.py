from django.contrib.auth import get_user_model
from django.core.mail import send_mail, get_connection
from celery import shared_task
# from django_celery import settings
from django.conf import settings

@shared_task(bind=True)
def send_mail_func(self):
    # timezone.localtime(users.date_time) + timedelta(days=2)
    # users = get_user_model().objects.all()
    # for user in users:
    mail_subject = "Hi, Celery User"
    message = "Stay jiggy and Breathe air."
    to_email = 'godwinadigun2@gmail.com'
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [to_email],
        fail_silently = False,
    )
    return "Done"