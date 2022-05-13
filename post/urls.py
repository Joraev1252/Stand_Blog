from django.urls import path

from . views import *

app_name = 'post'

urlpatterns = [
    path('add/', post_blog_views, name='add_post'),
    path('edit/<int:pk>/', edit_blog, name='edit_post'),
    path('delete/<int:pk>/', delete_blog, name='delete_post'),
    path('detail/<int:pk>/', detail_view, name='detail_blog'),
]