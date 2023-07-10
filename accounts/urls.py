from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
]