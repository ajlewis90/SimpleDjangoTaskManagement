from django.urls import path

from . import views # or i can write 'from tasks import views'

app_name = 'tasks'

# each url here points to the views inside my task app

urlpatterns = [
	# This url points to the view which gives the list of tasks
    # The third paramete i.e. 'name' is an alias for your url or view
    # You can keep the alias the same as the view name the url points to
    # or give it a different but meaningful name
    # We can use url aliases within templates or even within our python view code
    # Either to open a new view (in html) or for redirections (usually in python code)
    path('', views.task_list, name='task_list'),

    # This url points to the view where we create a new task
    path('new/', views.task_create, name='task_create'),

    # THis url points to the view where we see details of a particular task
    # It takes a parameter which is the task id or primary key of the tasks model
    path('<int:pk>/', views.task_detail, name='task_detail'),

    # This url points to the view which updates a particular task
    # For this we need to specifiy the task id or pk as parameter in this url
    path('edit/<int:pk>/', views.task_update, name='task_update'),

    #This url points to the view which deletes a particular task
    # For this we need to specifiy the task id or pk as parameter in this url
    path('delete/<int:pk>', views.task_delete, name='task_delete'),
]