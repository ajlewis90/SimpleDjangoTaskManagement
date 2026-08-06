"""
Form used for both creating and editing a task.
"""
from django import forms

from .models import Task

# This is a model form
'''
A model form creates its fields based on a model you have written or its 
already inbuilt in django eg: AbstractUser (for auth_user table)
A django form can directly be loaded into an HTML template via a view function
from the corresponding views.py file
We pass the form as a context parameter to the template
So it can then be rendered (i.e. displayed) on your html template page

'''

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # We are only interested in 5 fields from the Task model class to be displayed
        fields = ('title', 'description', 'status', 'priority', 'due_date')
        # By default fields are just Text inputs
        # But if you want to change that then specify which particular fields
        # would need a different type of input widget like below
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }