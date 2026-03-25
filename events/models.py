from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
