from django.urls import path

from board import views

urlpatterns = [
    path('', views.index, name='index'),
]
