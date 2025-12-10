from django.shortcuts import render
from students.models import Student
from assignments.models import Assignment
from submissions.models import Submission
from reminders.models import Reminder

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'assignment_count': Assignment.objects.count(),
        'submission_count': Submission.objects.count(),
        'reminder_count': Reminder.objects.count(),
        'submissions': Submission.objects.select_related('student','assignment')[:10],
    }
    return render(request, 'dashboard.html', context)