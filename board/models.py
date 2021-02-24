from django.db import models


class Categorys(models.Model):
    categorys = models.CharField(max_length=10)
    name = models.CharField(max_length=40)


class Threads(models.Model):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    first_message = models.CharField(max_length=500)


class Messages(models.Model):
    thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
    messages = models.CharField(max_length=500)
    published = models.DateTimeField(auto_now_add=True)
