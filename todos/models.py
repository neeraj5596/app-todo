from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, blank=True)
    FEELING_CHOICES = [
        ("happy", "Happy"),
        ("sad", "Sad"),
        ("neutral", "Neutral"),
    ]
    feeling = models.CharField(max_length=10, choices=FEELING_CHOICES, default="neutral")
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
