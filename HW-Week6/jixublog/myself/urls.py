from django.urls import path
from myself import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]