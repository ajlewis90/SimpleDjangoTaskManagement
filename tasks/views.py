"""
Standard CRUD views for tasks, written as plain function based views.
There is no login check anywhere in this file, this version of the
app has no accounts at all, every visitor shares the same list of
tasks.
"""
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    """Show every task, with an optional search box and status filter."""
    tasks = Task.objects.all()

    # Simple search box on the list page, matches on title or
    # description so it is easy to find something without scrolling
    # through the whole list.
    query = request.GET.get('q', '')
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # Optional status filter, driven by the dropdown in the template.
    status = request.GET.get('status', '')
    if status:
        tasks = tasks.filter(status=status)

    context = {
        'tasks': tasks,
        'status_choices': Task.Status.choices,
        'current_status': status,
        'current_query': query,
    }
    return render(request, 'tasks/task_list.html', context)


def task_detail(request, pk):
    """Show the full details of a single task."""
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)


# View to create a new task
# Collects data from your model form and then packages it as an object
# i.e. the Task object and then saves it to the database
# So its gets saved as a task record
def task_create(request):
    """Add a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Task created.')
            return redirect('tasks:task_detail', pk=task.pk)
    else:
        form = TaskForm()

    context = {'form': form, 'page_heading': 'New task'}
    return render(request, 'tasks/task_form.html', context)


# Again it takes in data from your form for a particular task 
# You identify the task by its id or primary key
# If it does not exist, you get a 404 error
# But if it exists, we take the form object, convert it into a model object
# and save it to update the particular record/model object
def task_update(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated.')
            return redirect('tasks:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'page_heading': 'Edit task', 'task': task}
    return render(request, 'tasks/task_form.html', context)

# delete the task by passing id or say th eprimark key as parameter
# if it is not found, then give a 404 error
# else you delete that object i.e. record from your Task model i.e. table
def task_delete(request, pk):
    """Delete a task, after the user confirms on a separate page."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('tasks:task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
