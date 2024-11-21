from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    satiety = models.IntegerField(default=40)
    happiness = models.IntegerField(default=40)
    is_sleeping = models.BooleanField(default=False)

