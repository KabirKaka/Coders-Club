from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('myprofile/', views.profile, name='account-profile'),
    path('login/', views.login, name='account-login'),
    path('join-community/', views.joinCommunity, name='account-joincommunity'),
]