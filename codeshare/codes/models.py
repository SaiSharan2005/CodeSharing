from django.db import models

# Create your models here.

class Room(models.Model):
    Topic = models.CharField(max_length=200)
    Question = models.TextField(null = True, blank=True)
    Answer = models.TextField(null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Question = models.CharField(max_length=1000)
    def __str__(self):
        return self.Topic