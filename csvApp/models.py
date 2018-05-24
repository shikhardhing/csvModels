from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    detail = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.id