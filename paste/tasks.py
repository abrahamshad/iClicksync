from celery import shared_task
from .models import Paste
from django.utils import timezone
from datetime import timedelta

# @shared_task
# def delete_expired_pastes():
#     now = timezone.now()
#     pastes = Paste.objects.filter(is_active=True)
#     for paste in pastes:
#         if paste.is_expired():
#             paste.is_active = False
#             paste.save()


# from celery import shared_task
# from .models import Paste
# from django.utils import timezone

@shared_task
def delete_expired_pastes():
    now = timezone.now()
    Paste.objects.filter(is_active=True, created_at__lt=now - timedelta(minutes=Paste.expiration_time)).update(is_active=False)
