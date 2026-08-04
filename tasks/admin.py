from django.contrib import admin

from .models import Task #"." just means start from the same parent directory of this file
#from tasks.models import Task #Even this works

# Register your models here.
registered_models = [Task] #can add more models to this list

admin.site.register(registered_models)

