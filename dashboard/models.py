from django.db import models
from django.contrib.auth.models import User


class PlayableCharacter(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=18)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class InventoryItem(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField(default=10)
    description = models.TextField()
    weight = models.DecimalField(decimal_places=2, max_digits=1000)
    playable_character = models.ForeignKey(
        PlayableCharacter, on_delete=models.CASCADE)
