from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Kruk(models.Model):
    content = models.CharField(max_length=160)
    creation_date = models.DateTimeField(default=now)
    krukacz = models.ForeignKey(User, on_delete=models.CASCADE)


class KrukComment(models.Model):
    content = models.CharField(max_length=60)
    creation_date = models.DateTimeField(default=now)
    kruk = models.ForeignKey(Kruk, on_delete=models.SET_NULL, null=True)
    """Komentarze użytkownika zostają tak długo jak żyje użytkownik"""
    krukacz = models.ForeignKey(User, on_delete=models.CASCADE)

class Observer(models.Model):
    krukacz = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    observed_krukacz = models.ManyToManyField(User, related_name='observed_krukacz')

