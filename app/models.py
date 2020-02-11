from django.db import models

# Create your models here.
class EpochModel(models.Model):
    epochtime = models.DecimalField(decimal_places=0, max_digits=10)