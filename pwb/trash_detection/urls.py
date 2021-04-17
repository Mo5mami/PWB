from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path(r'trash-detection/inference/', views.TrashDetection.as_view()),
    
]

