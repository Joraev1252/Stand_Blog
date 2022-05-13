from django.urls import path

from . views import *

app_name = 'blog'

urlpatterns = [
    path('add/', post_blog, name='add_blog'),
    path('edit/<int:pk>/', edit_blog, name='edit_blog'),
    path('delete/<int:pk>/', delete_blog, name='delete_blog'),
    path('detail/<int:pk>/', detail_view, name='detail_blog'),
]