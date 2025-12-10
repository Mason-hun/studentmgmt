from django.db import models
from students.models import Student
from assignments.models import Assignment

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}"