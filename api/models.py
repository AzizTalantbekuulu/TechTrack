from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role = models.CharField(max_length=100)  # Добавляем поле role
    REQUIRED_FIELDS = ['role']

class Equipment(models.Model):
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=100)

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    speed = models.FloatField()
    pressure = models.FloatField()

class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='alerts', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
