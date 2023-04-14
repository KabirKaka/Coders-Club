from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('/selected', views.selected, name='gallery-selected'),
]