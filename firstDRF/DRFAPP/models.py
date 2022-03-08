from django.db import models
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone



class Patient(models.Model):
    USER_ID = models.CharField(max_length=30)
    TIMESTAMP = models.DateTimeField()
    HEART_RATE = models.IntegerField()
    RESP_RATE = models.IntegerField()
    ACTIVITY = models.IntegerField()

    def __str__(self):
        return self.USER_ID


