# define all url mappings related to users app
from django.urls import path, include
import django.contrib.auth.urls as auth_urls
from . import views

app_name = 'users'

urlpatterns = [
    path('', include(auth_urls)),
    path('register/', views.register, name='register'),
]
