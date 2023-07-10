from . import views
from django.urls import path

urlpatterns = [
   path('', views.view_building, name ='view_building'),
   path('post_building/', views.post_building, name = 'post-building'),
   path('my-posts/', views.manage_building_posts, name = 'manage_building_posts'),
   path('delete/<int:post_id>', views.delete_building_post, name = 'delete_building_post'),
   path('secure/<int:post_id>', views.secure_building, name= 'secure-building')
]