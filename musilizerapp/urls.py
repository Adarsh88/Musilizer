from django.conf.urls import url
from django.urls import path , include

from . import views



urlpatterns = [
    
    path('', views.index, name= 'index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^success$', views.success, name='success'),
    url(r'^retrieve$', views.retrieve, name='retrieve'),
    url(r'^play$', views.play, name='play'),
    url(r'^error$', views.error, name='error'),
]