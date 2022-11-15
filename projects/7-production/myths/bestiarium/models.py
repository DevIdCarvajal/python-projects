from django.db import models

# Schema
class Creatures(models.Model):
  name = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  weight = models.IntegerField()