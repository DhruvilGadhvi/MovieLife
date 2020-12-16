from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sorted/', views.sort_popularity, name='index'),
]