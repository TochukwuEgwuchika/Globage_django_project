from . import views
from django.urls import path

urlpatterns = [
    path('join/', views.become_service_personnel, name = 'become_service_personnel'),
    path('hire/', views.hire_services, name = 'hire_services'),
    path('hire/<int:id>', views.hire, name = 'hire'),
    path('work_samples/<int:id>', views.view_work_samples, name = 'view_work_samples')
]