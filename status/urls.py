from . import views
from django.urls import path


urlpatterns = [
    path('status/', views.status, name = 'status')
]