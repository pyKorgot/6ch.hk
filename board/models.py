from django.db import models


class Thread(models.Model):
    messages = models.CharField(max_length=500)
