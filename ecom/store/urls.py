from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>', views.product, name='product'),
    path('planos/', views.planos, name='planos'),
    path('fachadas/', views.fachadas, name='fachadas'),
]