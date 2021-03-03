from django.urls import path

from board import views

urlpatterns = [
    path('<str:name>/<str:thread>/', views.thread_view, name='thread'),
    path('<str:name>/', views.threads_view, name='threads'),
    path('', views.index, name='index'),
]
