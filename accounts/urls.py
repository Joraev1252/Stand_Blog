from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', registration_view, name='register'),
    path('signin/', authentication, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('', starting, name='starting'),
]