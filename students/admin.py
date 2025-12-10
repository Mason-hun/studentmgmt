from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'reg_number', 'course')
    search_fields = ('name', 'reg_number', 'email')