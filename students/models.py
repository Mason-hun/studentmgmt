from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reg_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.reg_number})"