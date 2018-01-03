from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Survey(models.Model):
    created = models.DateTimeField()
    responses = JSONField()


    class Meta:
        verbose_name_plural = 'Surveys'
        ordering = ['-created']
