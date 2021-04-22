from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from asgiref.sync import sync_to_async


urlpatterns = [
    path(r'trash-detection/inference/', sync_to_async(views.TrashDetection.as_view())),
    
]

