from django.db import models


class Categorys(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categorys'
        verbose_name = 'Category'
        ordering = ['category']

    def __str__(self):
        return self.category


class Threads(models.Model):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    first_message = models.CharField(max_length=500)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Threads'
        verbose_name = 'Thread'
        ordering = ['category']

    def __str__(self):
        return self.name


class Messages(models.Model):
    thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'
        ordering = ['thread', 'published']

    def __str__(self):
        return self.message
