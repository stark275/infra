from django.db import models

class Engagement(models.Model):
    name = models.CharField(max_length=200)
    created = models.CharField(max_length=20)
    controlled = models.CharField(max_length=20)
    confirmed = models.CharField(max_length=20)
    canceled = models.BooleanField(default=False)

