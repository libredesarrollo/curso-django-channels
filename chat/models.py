from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=60, unique=True)
    users = models.ManyToManyField(User, related_name='rooms_joined', blank=True)

    def __str__(self):
        return self.name
