"""
Project level views. Right now this is just the home page, it lives
here rather than inside the tasks app since it is not really part of
task management, it is just the front door of the site.
"""
from django.shortcuts import render


def home(request):
    """Home page, just a simple welcome screen with a link to the task list."""
    return render(request, 'home.html')