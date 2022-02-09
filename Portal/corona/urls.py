from distutils.command.upload import upload
from unicodedata import name
from urllib.parse import urlparse
from django.urls import path, re_path
from . import views

app_name = 'corona'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('upload/', views.upload_test, name='upload_test')
]
