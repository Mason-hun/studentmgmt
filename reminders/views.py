from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm

def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/list.html', {'reminders': reminders})

def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/add.html', {'form': form, 'view_title': 'Add'})

def edit_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/edit.html', {'form': form, 'view_title': 'Edit'})

def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminders/delete.html', {'reminder': reminder})