from . import views
from django.urls import path , include

app_name = 'musilizer'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('register', views.register),
    path('login', views.login),
]
