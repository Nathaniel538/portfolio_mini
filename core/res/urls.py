from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index, name='index'),
    path('post',views.post, name='post'),
    path('chat', views.chat, name='chat'),
    path('completed',views.completed, name='completed'),
]