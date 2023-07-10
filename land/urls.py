from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_land, name='view_land'),
    path('post_land/', views.post_land, name ='post_land'),
   path('my-posts/', views.manage_land_posts, name = 'manage_land_posts'),
   path('delete/<int:post_id>', views.delete_land_post, name = 'delete_land_post'),
   path('secure/<int:post_id>', views.secure_land, name = 'secure-land')
]