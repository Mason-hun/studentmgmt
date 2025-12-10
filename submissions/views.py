from django.shortcuts import render, redirect, get_object_or_404
from .models import Submission
from .forms import SubmissionForm

def submission_list(request):
    submissions = Submission.objects.select_related('student', 'assignment').all()
    return render(request, 'submissions/list.html', {'submissions': submissions})

def add_submission(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_list')
    else:
        form = SubmissionForm()
    return render(request, 'submissions/add.html', {'form': form, 'view_title': 'Add'})

def edit_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('submission_list')
    else:
        form = SubmissionForm(instance=submission)
    return render(request, 'submissions/edit.html', {'form': form, 'view_title': 'Edit'})

def delete_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        submission.delete()
        return redirect('submission_list')
    return render(request, 'submissions/delete.html', {'submission': submission})