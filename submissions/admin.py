from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'assignment', 'submitted_on', 'grade', 'status')
    list_filter = ('status', 'submitted_on')
    search_fields = ('student__name', 'assignment__title')