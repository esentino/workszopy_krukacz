from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Kruk(models.Model):
    content = models.CharField(max_length=160)
    creation_date = models.DateTimeField(default=now)
    krukacz = models.ForeignKey(User, on_delete=models.CASCADE)

