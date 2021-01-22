from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_welcome),
    path('home/', views.welcome_page, name='welcome_page'),
    path('test/', views.test_page),
]
