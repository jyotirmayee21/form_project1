"""
URL configuration for formproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formcreation/',formcreation,name='formcreation'),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_Webpage/',insert_Webpage,name='insert_Webpage'),
    path('insert_accessrecord/',insert_accessrecord,name='insert_accessrecord'),
    path('select_topic/',select_topic,name='select_topic'),
    path('checkbox/',checkbox,name='checkbox'),
    path('update_webpage/',update_webpage,name='update_webpage'),
    path('delete_webpage/',delete_webpage,name='delete_webpage'),

]
