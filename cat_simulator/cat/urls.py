from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('cat_stats/', views.cat_stats, name='cat_stats'),
    path('action/', views.cat_action, name='cat_action'),
]