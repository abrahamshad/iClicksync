from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import random
import string
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from .validators import validate_file_extension, validate_file_size
# from django_summernote.fields import SummernoteTextField

def generate_code():
    return ''.join(random.choices(string.digits, k=13))

EXPIRATION_CHOICES = [
    (5, '5 min'),
    (10, '10 min'),
    (30, '30 min'),
    (60, '1 hour'),
    (120, '2 hour'),
    (720, '12 hour'),
    (1440, '1 day'),
    (10080, '7 day'),
    (43200, '30 day'),
]

class Paste(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    code = models.CharField(max_length=13, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_time = models.IntegerField(choices=EXPIRATION_CHOICES)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[validate_file_size, validate_file_extension])

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        if self.password:
            return check_password(raw_password, self.password)
        return True

    def is_expired(self):
        expiration_time = self.created_at + timedelta(minutes=self.expiration_time)
        return expiration_time < timezone.now()
