from . import views
from django.urls import path

urlpatterns = [
    path('get_verified/', views.user_verification, name = 'user_verification')
]