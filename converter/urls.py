from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='site-home'),
    path('convertPage/', views.convertPage, name='site-home2'),
]
