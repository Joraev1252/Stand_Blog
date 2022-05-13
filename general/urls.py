from django.urls import path

from general.views import *

app_name = 'general'

urlpatterns = [
    path('home/', main_home, name='home_page'),
    path('about/', about, name='about_page'),
    path('blog/', blog, name='blog_page'),
    path('detail/', detail, name='blog_detail'),
    path('contact/', contact, name='blog_contact')
]