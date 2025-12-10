from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title