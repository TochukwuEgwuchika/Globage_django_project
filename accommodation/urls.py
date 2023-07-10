from . import views
from django.urls import path

urlpatterns = [
    path('', views.find_accommodation, name='find_accommodation'),
    path('post/', views.post_accommodation, name = 'post-accommodation'),
    path('my-posts/', views.manage_accommodation_posts, name= 'manage_accommodation_posts'),
    path('delete/<int:post_id>', views.delete_accommodation_post, name= 'delete_accommodation_post'),
    path('secure/<int:post_id>', views.secure_accommodation, name = 'secure-accommodation')
]