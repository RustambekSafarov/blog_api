from django.urls import path
from .views import post_list, add_post, post_by_id, update_post, delete_post

urlpatterns = [
    path('',post_list,name='posts'),
    path('add/',add_post, name='create post'),
    path('post/<int:id>/',post_by_id, name='post'),
    path('post/<int:id>/update/',update_post, name='update post'),
    path('post/<int:id>/delete/', delete_post, name='delete post'),
]