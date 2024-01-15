from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.loginUser, name='login'),
    path('loguot', views.logoutUser, name='logout'),
    path('register/', views.registerUseer, name='register'),
]