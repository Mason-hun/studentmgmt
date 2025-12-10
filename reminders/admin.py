from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date')
    list_filter = ('due_date',)
    search_fields = ('title', 'description')