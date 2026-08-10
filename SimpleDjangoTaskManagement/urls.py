"""
URL configuration for SimpleDjangoTaskManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls), #admin url path configuration
    path('', views.home, name='home'), #main project's default url configuration
    path('tasks/', include('tasks.urls')), #base url to the tasks app

]


"""
Hypothethically if I had other apps like 'calendars' or 'product'
then i can have paths like this:
path('calendars/', include('calendars.urls')),
path('products/', include('products.urls')),
....and so on
"""
